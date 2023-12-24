from domain.services.controllers import DatabaseController
from domain.services.factories import ProductRepository
from domain.services.factories import (
    DatabaseConnectionFactory,
    DatabaseControllerFactory
)
from dataclasses import dataclass

@dataclass
class Injection:
    database_connection_factory: DatabaseConnectionFactory
    database_controller_factory: DatabaseControllerFactory
    database_controller: DatabaseController
    product_repository: ProductRepository