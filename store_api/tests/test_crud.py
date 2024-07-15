# tests/test_crud.py
import pytest
from bson import ObjectId
from app.crud import create_product, update_product, delete_product, list_products, get_product
from app.schemas import ProductSchema, UpdateProductSchema
from app.database import product_collection

@pytest.fixture
async def test_product():
    product = ProductSchema(name="Test Product", quantity=100, price=1000.0, status="available")
    created_product = await create_product(product)
    yield created_product
    await product_collection.delete_one({"_id": ObjectId(created_product["id"])})

@pytest.mark.asyncio
async def test_create_product():
    product = ProductSchema(name="Product1", quantity=10, price=100, status="available")
    created_product = await create_product(product)
    assert created_product["name"] == "Product1"
    await product_collection.delete_one({"_id": ObjectId(created_product["id"])})

@pytest.mark.asyncio
async def test_get_product(test_product):
    fetched_product = await get_product(test_product["id"])
    assert fetched_product["name"] == test_product["name"]

@pytest.mark.asyncio
async def test_update_product(test_product):
    update_data = UpdateProductSchema(price=2000.0)
    updated_product = await update_product(test_product["id"], update_data)
    assert updated_product["price"] == 2000.0

@pytest.mark.asyncio
async def test_delete_product(test_product):
    deleted_product = await delete_product(test_product["id"])
    assert deleted_product["id"] == test_product["id"]
    with pytest.raises(Exception):
        await get_product(test_product["id"])

@pytest.mark.asyncio
async def test_list_products():
    product1 = ProductSchema(name="Product1", quantity=10, price=6000, status="available")
    product2 = ProductSchema(name="Product2", quantity=20, price=7000, status="available")
    created_product1 = await create_product(product1)
    created_product2 = a
