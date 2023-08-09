from pydantic import BaseModel, root_validator,Field
from datetime import datetime, timedelta
from beanie import before_event, Replace, Insert

class Card(BaseModel):
    network: str
    phone_number: str
    price: float
    category: str
    detail: str
    date: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()

