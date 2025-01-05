# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import functools
from typing import Any, List, Optional, cast, Union
from typing_extensions import Literal

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
from ..._base_client import make_request_options
from ...lib import polling
from ...types.document_ai import parse_create_job_params
from ...types.document_ai.parse_create_job_response import ParseCreateJobResponse
from ...types.document_ai.parse_retrieve_job_response import ParseRetrieveJobResponse, FailedJob, SuccessfulParsingJob

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def create_job(
        self,
        *,
        file_id: str,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseCreateJobResponse:
        """
        Start a parse job for the provided file.

        Args: params: ParseJobCreateParams The parameters for creating a parse job.

        Returns: ParsingJob: The created parse job.

        Args:
          file_id: The ID of the file to parse

          chunking_strategy: The strategy to use for chunking the content

          element_types: The elements to extract from the document

          return_format: The format of the returned content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ParseCreateJobResponse,
            self._post(
                "/v1/document-ai/parse",
                body=maybe_transform(
                    {
                        "file_id": file_id,
                        "chunking_strategy": chunking_strategy,
                        "element_types": element_types,
                        "return_format": return_format,
                    },
                    parse_create_job_params.ParseCreateJobParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseCreateJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseRetrieveJobResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: ParsingJob: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            ParseRetrieveJobResponse,
            self._get(
                f"/v1/document-ai/parse/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseRetrieveJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def poll(
            self,
            job_id: str,
            *,
            poll_interval_ms: int | NotGiven = NOT_GIVEN,
            poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> ParseRetrieveJobResponse:
        """
        Poll for a parse job's status until it reaches a terminal state.
        Args:
            job_id: The ID of the parse job to poll
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The parse job object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve_job, job_id),
            condition=lambda res: res.status == "successful" or res.status == "failed",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
            self,
            *,
            file_id: str,
            chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
            element_types: Optional[List[str]] | NotGiven = NOT_GIVEN,
            return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
            poll_interval_ms: int | NotGiven = NOT_GIVEN,
            poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> Union[FailedJob, SuccessfulParsingJob]:
        """
        Create a parse job and wait for it to complete.
        Args:
            file_id: The ID of the file to parse
            chunking_strategy: The strategy to use for chunking the content
            element_types: The elements to extract from the document
            return_format: The format of the returned content
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The parse job object once it reaches a terminal state
        """
        response = self.create_job(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
        )
        return self.poll(
            response.id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def create_job(
        self,
        *,
        file_id: str,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseCreateJobResponse:
        """
        Start a parse job for the provided file.

        Args: params: ParseJobCreateParams The parameters for creating a parse job.

        Returns: ParsingJob: The created parse job.

        Args:
          file_id: The ID of the file to parse

          chunking_strategy: The strategy to use for chunking the content

          element_types: The elements to extract from the document

          return_format: The format of the returned content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ParseCreateJobResponse,
            await self._post(
                "/v1/document-ai/parse",
                body=await async_maybe_transform(
                    {
                        "file_id": file_id,
                        "chunking_strategy": chunking_strategy,
                        "element_types": element_types,
                        "return_format": return_format,
                    },
                    parse_create_job_params.ParseCreateJobParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseCreateJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseRetrieveJobResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: ParsingJob: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            ParseRetrieveJobResponse,
            await self._get(
                f"/v1/document-ai/parse/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseRetrieveJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def poll(
            self,
            job_id: str,
            *,
            poll_interval_ms: int | NotGiven = NOT_GIVEN,
            poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> ParseRetrieveJobResponse:
        """
        Poll for a parse job's status until it reaches a terminal state.
        Args:
            job_id: The ID of the parse job to poll
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The parse job object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve_job, job_id),
            condition=lambda res: res.status == "successful" or res.status == "failed",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
            self,
            *,
            file_id: str,
            chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
            element_types: Optional[List[str]] | NotGiven = NOT_GIVEN,
            return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
            poll_interval_ms: int | NotGiven = NOT_GIVEN,
            poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> Union[FailedJob, SuccessfulParsingJob]:
        """
        Create a parse job and wait for it to complete.
        Args:
            file_id: The ID of the file to parse
            chunking_strategy: The strategy to use for chunking the content
            element_types: The elements to extract from the document
            return_format: The format of the returned content
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The parse job object once it reaches a terminal state
        """
        response = await self.create_job(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
        )
        return await self.poll(
            response.id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create_job = to_raw_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = to_raw_response_wrapper(
            parse.retrieve_job,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create_job = async_to_raw_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = async_to_raw_response_wrapper(
            parse.retrieve_job,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create_job = to_streamed_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = to_streamed_response_wrapper(
            parse.retrieve_job,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create_job = async_to_streamed_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = async_to_streamed_response_wrapper(
            parse.retrieve_job,
        )
