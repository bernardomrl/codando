from dataclasses import dataclass

@dataclass
class DependencyInjection:
    database_connection_factory: str
    database_controller_factory: str
    database_controller: str
    product_repository: str