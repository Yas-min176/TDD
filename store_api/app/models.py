# app/models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    quantity: int
    price: float
    status: str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
