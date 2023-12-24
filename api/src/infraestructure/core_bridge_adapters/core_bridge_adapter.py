from infraestructure.database_connection_factories import DatabaseConnectionFactoryPostgres
from infraestructure.database_controller_factories import DatabaseControllerFactoryPostgres
from infraestructure.database_controllers import DatabaseControllerPostgres
from infraestructure.product_repositories import ProductRepositoryPostgres
from domain.models import (
    DependencyInjection,
    Injection
)

class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "database_connection_factory_postgres": DatabaseConnectionFactoryPostgres(),
            "database_controller_factory_postgres": DatabaseControllerFactoryPostgres(),
            "database_controller_postgres": DatabaseControllerPostgres(),
            "product_repository_postgres": ProductRepositoryPostgres()
        }

    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
            return Injection(
                self.adapters[dependency_injection.database_connection_factory],
                self.adapters[dependency_injection.database_controller_factory],
                self.adapters[dependency_injection.database_controller],
                self.adapters[dependency_injection.product_repository]
            )