from pydantic import BaseModel, root_validator
from datetime import datetime

class Card(BaseModel):
    network: str
    phone_number: str
    price: float
    category: str
    detail: str
    date: str

    @root_validator(pre=True)
    def set_default_date(cls, values):
        if "date" not in values:
            values["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return values
