from typing import Optional

from pydantic import BaseModel


class Error(BaseModel):
    field: str = None
    message: str = None
    code: int = None
    value: Optional[str] = None


class ResponseError(BaseModel):
    status: str = None
    error: Error = None
