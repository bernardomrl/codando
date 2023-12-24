from infraestructure.core_dependency_injection_factories import CoreDependencyInjectionFactoryJson
from infraestructure.core_bridge_adapters import CoreBridgeAdapter
from domain.models import Product
from domain.usecases import (
    GetInjection,
    GetDatabaseController
)

def product_group(id: int, name: str, desc: str, quantity: int, price: float) -> Product:
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge_adapter = CoreBridgeAdapter()

    get_injection = GetInjection(
        core_bridge_adapter,
        core_dependency_injection_factory
    )

    injection = get_injection.call()
    database_controller = GetDatabaseController(
        injection.database_connection_factory
    )

    database_controller = database_controller.call()

    database_controller.execute()