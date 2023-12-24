from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str
    desc: str
    quantity: int
    price: float
    