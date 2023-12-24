from domain.models import Product

class ProductFactory:
    def call(self) -> Product:
        raise NotImplementedError()