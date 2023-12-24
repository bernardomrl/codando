from dataclasses import asdict
from fastapi import APIRouter
from domain.groups import product_group

product_router = APIRouter()

@product_router.post("/product/create/{product}")
def create_product_route(id: int, name: str, desc: str, quantity: int, price: float):
    product = product_group(id, name, desc, quantity, price)
    return asdict(product)

@product_router.get("/product/delete/{product_id}")
def delete_product_route(product_id: int):
    product = product_group(product_id)
    return asdict(product)

@product_router.post("/product/update/{product_id}")
def update_product_route(product_id: int, name: str, desc: str, quantity: int, price: float):
    product = product_group(product_id, name, desc, quantity, price)
    return asdict(product)

@product_router.get("/product/get")
def get_all_products_route():
    product = product_group()
    return asdict(product)