from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class PostSchema(BaseModel):
    id: Optional[str]
    name: str
    description: str
    latitude: float
    longitude: float
    date_created: Optional[date] = datetime.now()
    date_updated: Optional[datetime] = datetime.now()


