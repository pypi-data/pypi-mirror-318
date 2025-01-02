from typing import List, Optional

from pydantic import BaseModel


class Location(BaseModel):
    line: int
    column: int


class Tracing(BaseModel):
    trace_id: str


class ErrorExtensions(BaseModel):
    name: str
    source: str
    code: int
    kind: str
    retry_after: Optional[int] = None
    tracing: Tracing


class Error(BaseModel):
    message: str
    locations: Optional[List[Location]] = []
    path: Optional[List[str]] = []
    extensions: ErrorExtensions
    code: int
    kind: str
    name: str
    source: str
    retry_after: Optional[int] = None
    tracing: Tracing


class ErrorResponse(BaseModel):
    errors: List[Error]
