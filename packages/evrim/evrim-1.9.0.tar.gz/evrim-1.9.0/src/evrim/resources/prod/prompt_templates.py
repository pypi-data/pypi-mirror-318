# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.prod import prompt_template_save_params
from ..._base_client import make_request_options
from ...types.template import Template

__all__ = ["PromptTemplatesResource", "AsyncPromptTemplatesResource"]


class PromptTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return PromptTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return PromptTemplatesResourceWithStreamingResponse(self)

    def save(
        self,
        *,
        fields: Iterable[Dict[str, object]],
        name: str,
        questions: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/prompt-template/save/",
            body=maybe_transform(
                {
                    "fields": fields,
                    "name": name,
                    "questions": questions,
                },
                prompt_template_save_params.PromptTemplateSaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )


class AsyncPromptTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncPromptTemplatesResourceWithStreamingResponse(self)

    async def save(
        self,
        *,
        fields: Iterable[Dict[str, object]],
        name: str,
        questions: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Template:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/prompt-template/save/",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "name": name,
                    "questions": questions,
                },
                prompt_template_save_params.PromptTemplateSaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )


class PromptTemplatesResourceWithRawResponse:
    def __init__(self, prompt_templates: PromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.save = to_raw_response_wrapper(
            prompt_templates.save,
        )


class AsyncPromptTemplatesResourceWithRawResponse:
    def __init__(self, prompt_templates: AsyncPromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.save = async_to_raw_response_wrapper(
            prompt_templates.save,
        )


class PromptTemplatesResourceWithStreamingResponse:
    def __init__(self, prompt_templates: PromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.save = to_streamed_response_wrapper(
            prompt_templates.save,
        )


class AsyncPromptTemplatesResourceWithStreamingResponse:
    def __init__(self, prompt_templates: AsyncPromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.save = async_to_streamed_response_wrapper(
            prompt_templates.save,
        )
