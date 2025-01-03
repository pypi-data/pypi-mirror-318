# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.prod.blank_template import BlankTemplate

__all__ = ["TemplateResource", "AsyncTemplateResource"]


class TemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return TemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return TemplateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlankTemplate:
        return self._post(
            "/prod/v0/blank/template/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlankTemplate,
        )


class AsyncTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncTemplateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlankTemplate:
        return await self._post(
            "/prod/v0/blank/template/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlankTemplate,
        )


class TemplateResourceWithRawResponse:
    def __init__(self, template: TemplateResource) -> None:
        self._template = template

        self.create = to_raw_response_wrapper(
            template.create,
        )


class AsyncTemplateResourceWithRawResponse:
    def __init__(self, template: AsyncTemplateResource) -> None:
        self._template = template

        self.create = async_to_raw_response_wrapper(
            template.create,
        )


class TemplateResourceWithStreamingResponse:
    def __init__(self, template: TemplateResource) -> None:
        self._template = template

        self.create = to_streamed_response_wrapper(
            template.create,
        )


class AsyncTemplateResourceWithStreamingResponse:
    def __init__(self, template: AsyncTemplateResource) -> None:
        self._template = template

        self.create = async_to_streamed_response_wrapper(
            template.create,
        )
