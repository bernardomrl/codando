from backend.src.domain.models import Product
from backend.src.domain.services.controllers import DatabaseController
from domain.services.controllers import DatabaseController
from domain.services.repositories import ProductRepository
from domain.models import Product

class ProductRepositoryPostgres(ProductRepository):
    def create_product(self, product: Product, database_controller: DatabaseController):
        try:
            database_controller.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (product.name, product.quantity, product.price)) # Query para criar produto.
            return "Product created successfully!"
        except Exception as e:
            raise Exception("Error creating product: {}".format(str(e)))

    def get_product_by_id(self, product_id: int, database_controller: DatabaseController):
        product = database_controller.execute("SELECT product WHERE product_id = %s", (product_id, )) # Query para obter um produto pelo id.
        return Product(**product)
    
    def delete_product(self, product_name: str, database_controller: DatabaseController):
        try:
            database_controller.execute("DELETE FROM products WHERE name = %s", (product_name, )) # Query para deletar um produto pelo nome.
            return "Product deleted successfully!"
        except Exception as e:
            raise Exception("Error deleting product: {}".format(str(e)))
        
    def update_product(self, product: Product, product_id: str, database_controller: DatabaseController):
        try:
            database_controller.execute("UPDATE products SET name = %s, quantity = %s, price = %s WHERE product_id = %s", (product.name, product.quantity, product.price, product_id))
            return "Product updated successfully!"
        except Exception as e:
            raise Exception("Error updating product: {}".format(str(e)))