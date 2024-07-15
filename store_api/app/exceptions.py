# app/exceptions.py
from fastapi import HTTPException

class ProductNotFoundException(HTTPException):
    def __init__(self, id: str):
        super().__init__(status_code=404, detail=f"Product {id} not found")
