from pydantic import BaseModel, Field
from TradeAPI.Models.Side import Side

class EModel(BaseModel):
    id: int = Field(ge=0)
    new_id: int = Field(ge=0)
    new_user_id: int = Field(ge=0)
    new_currency: str = Field(min_length=3, max_length=3)
    new_side: Side
    new_price: float = Field(ge=0)
    amount: float = Field(ge=0)