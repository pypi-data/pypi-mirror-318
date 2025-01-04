from typing import Dict, Optional
from datetime import datetime
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId


class Agent(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    name: str
    description: str
    creator_id: str
    model_configuration: Dict
    system_prompt: Optional[str]
    token_address: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "active"
    domain: Optional[str]
    monthly_requests: int = 0

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

    @classmethod
    async def get(cls, agent_id: str):
        db = AsyncIOMotorClient().ethernal
        doc = await db.agents.find_one({"_id": ObjectId(agent_id)})
        return cls(**doc) if doc else None

    async def save(self):
        db = AsyncIOMotorClient().ethernal
        self.updated_at = datetime.utcnow()
        await db.agents.update_one(
            {"_id": ObjectId(self.id)},
            {"$set": self.dict(exclude={"id"})},
            upsert=True
        )