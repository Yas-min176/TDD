# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    name: str
    quantity: int
    price: float
    status: str

class UpdateProductSchema(BaseModel):
    name: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    status: Optional[str]
