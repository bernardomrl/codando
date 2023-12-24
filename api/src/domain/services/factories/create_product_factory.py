from domain.models import Product

class CreateProductFactory:
    def call(Self) -> Product:
        raise NotImplementedError()