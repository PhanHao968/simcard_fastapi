from pydantic import BaseModel, root_validator,Field
from datetime import datetime, timedelta
from beanie import before_event, Replace, Insert

class Sim(BaseModel):
    network: str
    phone_number: str = Field(..., description="Phone number is required")
    price: float
    category: str
    detail: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()

