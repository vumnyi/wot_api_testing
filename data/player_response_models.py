from typing import List

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
