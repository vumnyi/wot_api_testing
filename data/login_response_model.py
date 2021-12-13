from typing import List

from pydantic import BaseModel


class Meta(BaseModel):
    count: int = None


class Data(BaseModel):
    location: str = None


class LoginResponse(BaseModel):
    status: str = None
    meta: Meta = None
    data: Data = None
