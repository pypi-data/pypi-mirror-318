# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreListResponse", "Data", "DataExpiresAfter", "DataFileCounts", "Pagination"]


class DataExpiresAfter(BaseModel):
    anchor: Optional[Literal["last_used_at"]] = None
    """Anchor date for the expiration policy"""

    days: Optional[int] = None
    """Number of days after which the vector store expires"""


class DataFileCounts(BaseModel):
    canceled: Optional[int] = None
    """Number of files whose processing was canceled"""

    failed: Optional[int] = None
    """Number of files that failed processing"""

    in_progress: Optional[int] = None
    """Number of files currently being processed"""

    successful: Optional[int] = None
    """Number of successfully processed files"""

    total: Optional[int] = None
    """Total number of files"""


class Data(BaseModel):
    id: str
    """Unique identifier for the vector store"""

    created_at: datetime
    """Timestamp when the vector store was created"""

    name: str
    """Name of the vector store"""

    updated_at: datetime
    """Timestamp when the vector store was last updated"""

    description: Optional[str] = None
    """Detailed description of the vector store's purpose and contents"""

    expires_after: Optional[DataExpiresAfter] = None
    """Represents an expiration policy for a vector store."""

    expires_at: Optional[datetime] = None
    """Optional expiration timestamp for the vector store"""

    file_counts: Optional[DataFileCounts] = None
    """Counts of files in different states"""

    last_active_at: Optional[datetime] = None
    """Timestamp when the vector store was last used"""

    metadata: Optional[object] = None
    """Additional metadata associated with the vector store"""

    object: Optional[Literal["vector_store"]] = None
    """Type of the object"""


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Offset of the first item to return"""

    total: Optional[int] = None
    """Total number of items available"""


class VectorStoreListResponse(BaseModel):
    data: List[Data]
    """The list of vector stores"""

    pagination: Pagination
    """Pagination model that includes total count of items."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
