# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import ProductSchema, UpdateProductSchema
from app.crud import create_product, update_product, delete_product, list_products, get_product

app = FastAPI()

@app.post("/products/")
async def create_product_endpoint(product: ProductSchema):
    return await create_product(product)

@app.get("/products/")
async def list_products_endpoint(price_min: float = None, price_max: float = None):
    return await list_products(price_min, price_max)

@app.get("/products/{id}/")
async def get_product_endpoint(id: str):
    return await get_product(id)

@app.patch("/products/{id}/")
async def update_product_endpoint(id: str, product: UpdateProductSchema):
    return await update_product(id, product)

@app.delete("/products/{id}/")
async def delete_product_endpoint(id: str):
    return await delete_product(id)
