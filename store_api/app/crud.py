# app/crud.py
from app.database import product_collection, product_helper, get_product
from app.schemas import ProductSchema, UpdateProductSchema
from bson.objectid import ObjectId
from fastapi import HTTPException
from datetime import datetime

async def create_product(product_data: ProductSchema) -> dict:
    product = await product_collection.insert_one(product_data.dict())
    new_product = await product_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)

async def update_product(id: str, data: UpdateProductSchema) -> dict:
    data = {k: v for k, v in data.dict().items() if v is not None}
    if data:
        data["updated_at"] = datetime.utcnow()
        updated_product = await product_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_product.modified_count == 1:
            return await get_product(id)
    raise HTTPException(status_code=404, detail=f"Product {id} not found")

async def delete_product(id: str):
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        await product_collection.delete_one({"_id": ObjectId(id)})
        return product_helper(product)
    raise HTTPException(status_code=404, detail=f"Product {id} not found")

async def list_products(price_min: float = None, price_max: float = None) -> list:
    query = {}
    if price_min is not None and price_max is not None:
        query["price"] = {"$gt": price_min, "$lt": price_max}
    products = await product_collection.find(query).to_list(100)
    return [product_helper(product) for product in products]
