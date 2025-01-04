from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Token(BaseModel):
    token_address: str
    agent_id: str
    name: str
    symbol: str
    total_supply: int
    decimals: int = 9
    created_at: datetime
    owner_address: str
    token_program_id: str = ""
    transactions: list = []
    price_history: list = []
    current_price: Optional[float]

    class Config:
        allow_population_by_field_name = True

    @classmethod
    async def get_by_address(cls, address: str):
        db = AsyncIOMotorClient().ethernal
        doc = await db.tokens.find_one({"token_address": address})
        return cls(**doc) if doc else None

    async def update_price(self, new_price: float):
        self.price_history.append({
            "price": new_price,
            "timestamp": datetime.utcnow()
        })
        self.current_price = new_price
        await self.save()

    async def save(self):
        db = AsyncIOMotorClient().ethernal
        await db.tokens.update_one(
            {"token_address": self.token_address},
            {"$set": self.dict()},
            upsert=True
        )