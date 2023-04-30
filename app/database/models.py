from pydantic import BaseModel
from typing import List


class EventIn(BaseModel):
    id: int
    type: str
    detail: str
    timestamp: str


class EventInCreate(BaseModel):
    type: str
    detail: str


class EventDb(EventIn):
    player_id: int


class PlayerInCreate(BaseModel):
    name: str


class PlayerIn(BaseModel):
    id: int
    name: str


class PlayerDb(PlayerIn):
    events: List[EventDb] = []
