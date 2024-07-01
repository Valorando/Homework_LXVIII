from pydantic import BaseModel, Field
from TradeAPI.Models.Side import Side

class IOModel(BaseModel):
    id: int = Field(ge=0)
    user_id: int = Field(ge=0)
    currency: str = Field(min_length=3, max_length=3)
    side: Side
    price: float = Field(ge=0)
    amount: float = Field(ge=0)