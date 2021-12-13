import datetime
from typing import List

from pydantic import BaseModel


class Data(BaseModel):
    access_token: str = None
    account_id: int = None
    expires_at: datetime.time = None


class ProlongateResponse(BaseModel):
    status: str = None
    data: List[Data] = None
