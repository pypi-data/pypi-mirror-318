# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from .template import (
    TemplateResource,
    AsyncTemplateResource,
    TemplateResourceWithRawResponse,
    AsyncTemplateResourceWithRawResponse,
    TemplateResourceWithStreamingResponse,
    AsyncTemplateResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BlankResource", "AsyncBlankResource"]


class BlankResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def template(self) -> TemplateResource:
        return TemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> BlankResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return BlankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlankResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return BlankResourceWithStreamingResponse(self)


class AsyncBlankResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def template(self) -> AsyncTemplateResource:
        return AsyncTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBlankResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBlankResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlankResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncBlankResourceWithStreamingResponse(self)


class BlankResourceWithRawResponse:
    def __init__(self, blank: BlankResource) -> None:
        self._blank = blank

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._blank.profile)

    @cached_property
    def template(self) -> TemplateResourceWithRawResponse:
        return TemplateResourceWithRawResponse(self._blank.template)


class AsyncBlankResourceWithRawResponse:
    def __init__(self, blank: AsyncBlankResource) -> None:
        self._blank = blank

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._blank.profile)

    @cached_property
    def template(self) -> AsyncTemplateResourceWithRawResponse:
        return AsyncTemplateResourceWithRawResponse(self._blank.template)


class BlankResourceWithStreamingResponse:
    def __init__(self, blank: BlankResource) -> None:
        self._blank = blank

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._blank.profile)

    @cached_property
    def template(self) -> TemplateResourceWithStreamingResponse:
        return TemplateResourceWithStreamingResponse(self._blank.template)


class AsyncBlankResourceWithStreamingResponse:
    def __init__(self, blank: AsyncBlankResource) -> None:
        self._blank = blank

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._blank.profile)

    @cached_property
    def template(self) -> AsyncTemplateResourceWithStreamingResponse:
        return AsyncTemplateResourceWithStreamingResponse(self._blank.template)
