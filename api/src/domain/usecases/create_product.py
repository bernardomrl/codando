from domain.services.factories import CreateProductFactory
from domain.models import Product

class CreateProduct:
    def __init__(self, create_product_factory: CreateProductFactory) -> None:
        self.create_product_factory = create_product_factory

    def call(self) -> Product:
        return self.create_product_factory.call()