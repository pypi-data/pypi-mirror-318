# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import (
    vector_store_list_params,
    vector_store_create_params,
    vector_store_search_params,
    vector_store_update_params,
    vector_store_question_answering_params,
)
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
from ...types.vector_store import VectorStore
from ...types.search_response import SearchResponse
from ...types.vector_store_list_response import VectorStoreListResponse
from ...types.vector_store_delete_response import VectorStoreDeleteResponse

__all__ = ["VectorStoresResource", "AsyncVectorStoresResource"]


class VectorStoresResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return VectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return VectorStoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[vector_store_create_params.ExpiresAfter] | NotGiven = NOT_GIVEN,
        file_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          description: Description of the vector store

          expires_after: Represents an expiration policy for a vector store.

          file_ids: Optional list of file IDs

          metadata: Optional metadata key-value pairs

          name: Name for the new vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores",
            body=maybe_transform(
                {
                    "description": description,
                    "expires_after": expires_after,
                    "file_ids": file_ids,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Get a vector store by ID.

        Args: vector_store_id: The ID of the vector store to retrieve.

        Returns: VectorStore: The response containing the vector store details.

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._get(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def update(
        self,
        vector_store_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[vector_store_update_params.ExpiresAfter] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Update a vector store by ID.

        Args: vector_store_id: The ID of the vector store to update.
        vector_store_update: VectorStoreCreate object containing the name, description,
        and metadata.

        Returns: VectorStore: The response containing the updated vector store details.

        Args:
          vector_store_id: The ID of the vector store

          description: New description

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          name: New name for the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._put(
            f"/v1/vector_stores/{vector_store_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreListResponse:
        """
        List all vector stores.

        Args: pagination: The pagination options.

        Returns: VectorStoreListResponse: The list of vector stores.

        Args:
          limit: Maximum number of items to return per page

          offset: Cursor from which to start returning items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store by ID.

        Args: vector_store_id: The ID of the vector store to delete.

        Returns: VectorStore: The response containing the deleted vector store details.

        Args:
          vector_store_id: The ID of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._delete(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    def question_answering(
        self,
        *,
        vector_store_ids: List[str],
        filters: Optional[vector_store_question_answering_params.Filters] | NotGiven = NOT_GIVEN,
        pagination: vector_store_question_answering_params.Pagination | NotGiven = NOT_GIVEN,
        qa_options: vector_store_question_answering_params.QaOptions | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        search_options: vector_store_question_answering_params.SearchOptions | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Question answering

        Args:
          vector_store_ids: IDs of vector stores to search

          filters: Filter or condition

          pagination: Pagination options

          qa_options: Question answering configuration options

          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          search_options: Search configuration options

          stream: Whether to stream the answer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores/question-answering",
            body=maybe_transform(
                {
                    "vector_store_ids": vector_store_ids,
                    "filters": filters,
                    "pagination": pagination,
                    "qa_options": qa_options,
                    "query": query,
                    "search_options": search_options,
                    "stream": stream,
                },
                vector_store_question_answering_params.VectorStoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def search(
        self,
        *,
        query: str,
        vector_store_ids: List[str],
        filters: Optional[vector_store_search_params.Filters] | NotGiven = NOT_GIVEN,
        pagination: vector_store_search_params.Pagination | NotGiven = NOT_GIVEN,
        search_options: vector_store_search_params.SearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Perform a search based on the provided query.

        Args: search_query: SearchQuery object containing the search parameters.

        Returns: SearchResponse: The response containing the search results and
        pagination details.

        Args:
          query: Search query text

          vector_store_ids: IDs of vector stores to search

          filters: Filter or condition

          pagination: Pagination options

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores/search",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "filters": filters,
                    "pagination": pagination,
                    "search_options": search_options,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )


class AsyncVectorStoresResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncVectorStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[vector_store_create_params.ExpiresAfter] | NotGiven = NOT_GIVEN,
        file_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          description: Description of the vector store

          expires_after: Represents an expiration policy for a vector store.

          file_ids: Optional list of file IDs

          metadata: Optional metadata key-value pairs

          name: Name for the new vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "expires_after": expires_after,
                    "file_ids": file_ids,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Get a vector store by ID.

        Args: vector_store_id: The ID of the vector store to retrieve.

        Returns: VectorStore: The response containing the vector store details.

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._get(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def update(
        self,
        vector_store_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[vector_store_update_params.ExpiresAfter] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Update a vector store by ID.

        Args: vector_store_id: The ID of the vector store to update.
        vector_store_update: VectorStoreCreate object containing the name, description,
        and metadata.

        Returns: VectorStore: The response containing the updated vector store details.

        Args:
          vector_store_id: The ID of the vector store

          description: New description

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          name: New name for the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._put(
            f"/v1/vector_stores/{vector_store_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "name": name,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreListResponse:
        """
        List all vector stores.

        Args: pagination: The pagination options.

        Returns: VectorStoreListResponse: The list of vector stores.

        Args:
          limit: Maximum number of items to return per page

          offset: Cursor from which to start returning items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/vector_stores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            cast_to=VectorStoreListResponse,
        )

    async def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store by ID.

        Args: vector_store_id: The ID of the vector store to delete.

        Returns: VectorStore: The response containing the deleted vector store details.

        Args:
          vector_store_id: The ID of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._delete(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    async def question_answering(
        self,
        *,
        vector_store_ids: List[str],
        filters: Optional[vector_store_question_answering_params.Filters] | NotGiven = NOT_GIVEN,
        pagination: vector_store_question_answering_params.Pagination | NotGiven = NOT_GIVEN,
        qa_options: vector_store_question_answering_params.QaOptions | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        search_options: vector_store_question_answering_params.SearchOptions | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Question answering

        Args:
          vector_store_ids: IDs of vector stores to search

          filters: Filter or condition

          pagination: Pagination options

          qa_options: Question answering configuration options

          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          search_options: Search configuration options

          stream: Whether to stream the answer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores/question-answering",
            body=await async_maybe_transform(
                {
                    "vector_store_ids": vector_store_ids,
                    "filters": filters,
                    "pagination": pagination,
                    "qa_options": qa_options,
                    "query": query,
                    "search_options": search_options,
                    "stream": stream,
                },
                vector_store_question_answering_params.VectorStoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def search(
        self,
        *,
        query: str,
        vector_store_ids: List[str],
        filters: Optional[vector_store_search_params.Filters] | NotGiven = NOT_GIVEN,
        pagination: vector_store_search_params.Pagination | NotGiven = NOT_GIVEN,
        search_options: vector_store_search_params.SearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchResponse:
        """
        Perform a search based on the provided query.

        Args: search_query: SearchQuery object containing the search parameters.

        Returns: SearchResponse: The response containing the search results and
        pagination details.

        Args:
          query: Search query text

          vector_store_ids: IDs of vector stores to search

          filters: Filter or condition

          pagination: Pagination options

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "filters": filters,
                    "pagination": pagination,
                    "search_options": search_options,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )


class VectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = to_raw_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = async_to_raw_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = async_to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._vector_stores.files)


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = to_streamed_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = async_to_streamed_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = async_to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._vector_stores.files)
