# tests/test_main.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.database import product_collection

@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/", json={"name": "Product1", "quantity": 10, "price": 100, "status": "available"})
    assert response.status_code == 200
    assert response.json()["name"] == "Product1"

@pytest.mark.asyncio
async def test_list_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_product():
    product = await product_collection.insert_one({"name": "Product1", "quantity": 10, "price": 100, "status": "available"})
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch(f"/products/{product.inserted_id}/", json={"price": 150})
    assert response.status_code == 200
    assert response.json()["price"] == 150

@pytest.mark.asyncio
async def test_delete_product():
    product = await product_collection.insert_one({"name": "Product1", "quantity": 10, "price": 100, "status": "available"})
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete(f"/products/{product.inserted_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Product1"
