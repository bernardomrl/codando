from domain.services.repositories import ProductRepository
from domain.services.controllers import DatabaseController
from domain.models import Product

class ProductRepositoryPostgres(ProductRepository):
    def create_product(self, product: Product, database_controller: DatabaseController):
        try:
            product = database_controller.execute("INSERT INTO products VALUES(%s, %s, %s, %s)", (product, ))
            return f"Product created, {Product(Product)}."
        except Exception as e:
            raise Exception(f"Error creating product, {e}.")
    
    def update_product(self, product: Product, database_controller: DatabaseController):
        try:
            product = database_controller.execute("UPDATE product SET name = %s, desc = %s, quantity = %s, price = %s WHERE id = %s", (product.name, product.desc, product.quantity, product.price, product.id))
            return f"Product ID: {product.id} updated."
        except Exception as e:
            raise Exception(f"Error updating product, {e}.")

    def delete_product(self, product: Product, database_controller: DatabaseController):
        try:    
            database_controller.execute("DELETE FROM products WHERE name = %s", (product.name,))
            return f"Product ID: {product.id} deleted"
        except Exception as e:
            raise Exception(f"Error deleting product, {e}.")

    def get_all_products(self, database_controller: DatabaseController) -> Product:
        try:
            products = database_controller.execute("SELECT * FROM products")
            return [Product(**product_data) for product_data in products]
        except Exception as e:
            raise Exception(f"Error getting all products, {e}.")