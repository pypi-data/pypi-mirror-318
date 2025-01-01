import random
import traceback
from typing import Optional

from promptflow._utils.logger_utils import flow_logger
from pydantic import BaseModel, ConfigDict, Field, field_serializer

from nest_gen_accelerator_azure.components.output_parsers import JsonOutputParser
from nest_gen_accelerator_azure.components.outputs import CallToAction, ExitStrategy
from nest_gen_accelerator_azure.exceptions import (
    ContentPolicyViolationException,
    InvalidLLMResponseException,
)


class ContentFilterResults(BaseModel):
    prompt_results: dict
    completion_results: dict


class LLMResponse(BaseModel):
    """LLMResponse class encapsulating the response structure and parsing logic."""

    content: str = Field(alias="content")
    call_to_action: CallToAction = Field(alias="callToAction")
    exit_strategy: ExitStrategy = Field(alias="exitStrategy")
    model_details: dict = Field(alias="modelStats")
    content_filter_result: Optional[ContentFilterResults] = Field(
        alias="contentFilterResult", default=None
    )

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        protected_namespaces=(),
    )

    @field_serializer("call_to_action", when_used="json")
    def serialize_call_to_action(self, call_to_action: CallToAction) -> dict:
        return call_to_action.model_dump(exclude_none=True)

    @field_serializer("exit_strategy", when_used="json")
    def serialize_exit_strategy(self, exit_strategy: ExitStrategy) -> str:
        return exit_strategy.value

    @classmethod
    def validate_response_structure(cls, llm_response: dict) -> None:
        """Validates the LLM response structure has all required fields."""
        if not isinstance(llm_response, dict):
            raise InvalidLLMResponseException("LLM response must be a dictionary")

        # Check main required keys
        if not all(
            key in llm_response for key in ["choices", "model", "usage", "params"]
        ):
            raise InvalidLLMResponseException(
                "Missing required top-level keys in LLM response"
            )

        # Validate choices structure
        choices = llm_response.get("choices", [])
        if not choices or not isinstance(choices[0], dict):
            raise InvalidLLMResponseException("Invalid choices structure")

        # Validate message structure
        message = choices[0].get("message", {})
        if not isinstance(message, dict) or "content" not in message:
            raise InvalidLLMResponseException("Invalid message structure")

        # Validate usage structure
        usage = llm_response.get("usage", {})
        required_usage = ["prompt_tokens", "completion_tokens", "total_tokens"]
        if not all(key in usage for key in required_usage):
            raise InvalidLLMResponseException("Missing required usage statistics")

    @classmethod
    def create_error_response(
        cls,
        message: str,
        exit_strategy: ExitStrategy,
        llm_response: dict,
        content_filter_result: Optional[ContentFilterResults] = None,
    ) -> "LLMResponse":
        """Creates a standardized error response."""
        return cls(
            content=message,
            call_to_action=CallToAction(type="NONE"),
            exit_strategy=exit_strategy,
            model_details={
                "name": llm_response.get("model", ""),
                "prompt_tokens": llm_response.get("usage", {}).get(
                    "prompt_tokens", None
                ),
                "completion_tokens": 0,
                "total_tokens": llm_response.get("usage", {}).get("total_tokens", None),
                "params": llm_response.get("params", {}),
            },
            content_filter_result=content_filter_result,
        )

    @staticmethod
    def check_policy_violation(error_info: dict) -> None:
        """
        Checks content policy violations by raising an appropriate exception.

        Args:
            error_info: Dictionary containing error information.

        Raises:
            ContentPolicyViolationException: If a content policy violation is detected.
        """
        error = error_info.get("errorMessage", {}).get("error", {})
        if not error.get("code") == "content_filter":
            return

        raise ContentPolicyViolationException(error.get("message"), details=error)

    @classmethod
    def process_response_errors(cls, llm_response: dict) -> None:
        """Process any errors in the LLM response and raise appropriate exceptions."""
        error = llm_response.get("error", {})
        if not error:
            return

        response = error.get("response", {})

        cls.check_policy_violation(response)

        raise InvalidLLMResponseException(
            f"Error in LLM response ({error['type']}): {error['details']}"
        )

    @staticmethod
    def parse_content_filter_results(llm_response: dict) -> ContentFilterResults:
        """
        Parse content filter results from the LLM response.

        Args:
            llm_response: LLM response dictionary.

        Returns:
            ContentFilterResult: Content filter results.
        """
        prompt_results = {}
        completion_results = {}

        if "error" in llm_response:
            error = (
                llm_response["error"]
                .get("response", {})
                .get("errorMessage", {})
                .get("error", {})
            )
            trigger = error.get("param")
            content_filter_result = error.get("innererror", {}).get(
                "content_filter_result", {}
            )

            if trigger == "prompt":
                prompt_results = content_filter_result

            # TODO Determine how to handle completion content filter results

        else:
            prompt_results = llm_response.get("prompt_filter_results", [{}])[0].get(
                "content_filter_results", {}
            )
            completion_results = llm_response.get("choices", [{}])[0].get(
                "content_filter_results", {}
            )

        return ContentFilterResults(
            prompt_results=prompt_results, completion_results=completion_results
        )

    @classmethod
    def from_json(cls, llm_response: dict, tracking_id: str) -> "LLMResponse":
        try:
            cls.process_response_errors(llm_response)
            cls.validate_response_structure(llm_response)

            choices = llm_response["choices"]
            message = choices[0]["message"]
            message_content = JsonOutputParser.parse(message["content"])
            content = message_content.get("content")
            exit_strategy = message_content.get("exitStrategy")
            content_filter_results = cls.parse_content_filter_results(llm_response)

            call_to_action = CallToAction(**message_content.get("callToAction"))
            if not exit_strategy:
                # TODO Determine call to action through prompt
                if (
                    (
                        message_content
                        and message_content.get("callToAction", {}).get("type")
                        == "TO_LIVE_AGENT"
                    )
                    or (content and "dolce-gusto.fr/nous-contacter" in content)
                ) and (random.random() < 0.2):
                    flow_logger.info(
                        f"Overriding Call to Action to TO_LIVE_AGENT (Contact Us website mentioned in chat response)."
                    )
                    call_to_action = CallToAction(type="TO_LIVE_AGENT", value=True)

            model_details = {
                "name": llm_response["model"],
                "prompt_tokens": llm_response["usage"]["prompt_tokens"],
                "completion_tokens": llm_response["usage"]["completion_tokens"],
                "total_tokens": llm_response["usage"]["total_tokens"],
                "params": llm_response["params"],
            }

            response_instance = cls(
                content=content,
                call_to_action=call_to_action,
                exit_strategy=exit_strategy,
                model_details=model_details,
                content_filter_result=content_filter_results,
            )

            flow_logger.info(
                "Successfully parsed JSON response.",
                extra={
                    "content": content,
                    "tracking_id": tracking_id,
                    "total_tokens": model_details["total_tokens"],
                    "exit_strategy": exit_strategy,
                },
            )

            return response_instance

        except ContentPolicyViolationException as e:
            flow_logger.warning(
                "Content policy violation detected",
                extra={
                    "tracking_id": tracking_id,
                    "type": type(e).__name__,
                    "details": e.details,
                },
            )
            content_filter_results = cls.parse_content_filter_results(llm_response)
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to content policy restrictions.",
                ExitStrategy.OUT_OF_DOMAIN,
                llm_response,
                content_filter_result=content_filter_results,
            )

        except InvalidLLMResponseException as e:
            flow_logger.error(
                "Invalid LLM response structure",
                extra={"error": str(e), "tracking_id": tracking_id},
            )
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to an internal error.",
                ExitStrategy.ON_ERROR,
                llm_response,
            )

        except Exception as e:
            flow_logger.error(
                f"Unexpected error while parsing LLM response: {e}",
                extra={
                    "error": str(e),
                    "tracking_id": tracking_id,
                    "traceback": traceback.format_exc(),
                },
            )
            return cls.create_error_response(
                "I apologize, but I cannot provide an answer to that query due to an internal error.",
                ExitStrategy.ON_ERROR,
                llm_response,
            )

    def to_dict(self) -> dict:
        return self.model_dump(mode="json", by_alias=True)
