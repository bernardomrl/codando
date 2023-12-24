from domain.services.controllers import DatabaseController
from domain.models import Product

class ProductRepository:
    def create_product(self, product: Product, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def delete_product(self, product: Product, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def update_product(self, product: Product, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def get_product(self, name: str, database_controller: DatabaseController) -> Product:
        raise NotImplementedError()
    
    def get_all_products(self, database_controller: DatabaseController) -> list[str]:
        raise NotImplementedError()