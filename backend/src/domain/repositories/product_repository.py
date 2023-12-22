from domain.services.controllers import DatabaseController
from domain.models import Product

class ProductRepository:
    def create_product(self, product: Product, database_controller: DatabaseController):
        raise NotImplementedError()
    
    def get_product_by_id(self, product_id: int, database_controller: DatabaseController):
        raise NotImplementedError()