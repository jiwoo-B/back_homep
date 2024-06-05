from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id: int
    nickname: str
    item: str
    timestamp: datetime
