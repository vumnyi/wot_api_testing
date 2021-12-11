from typing import Optional, List

from pydantic import BaseModel


class Meta(BaseModel):
    count: int = None


class Data(BaseModel):
    nickname: str = None
    account_id: int = None


class PlayerResponse(BaseModel):
    status: str = None
    meta: Meta = None
    data: List[Data] = None


class Error(BaseModel):
    field: str = None
    message: str = None
    code: int = None
    value: Optional[str] = None


class PlayerResponseError(BaseModel):
    status: str = None
    error: Error = None
