# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from fastapi import HTTPException

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.store

product_collection = database.get_collection("products")

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "quantity": product["quantity"],
        "price": product["price"],
        "status": product["status"]
    }

async def get_product(id: str) -> dict:
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)
    else:
        raise HTTPException(status_code=404, detail=f"Product {id} not found")
