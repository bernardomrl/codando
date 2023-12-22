from infraestructure.database_controller_factories import DatabaseControllerFactoryPostgres
from infraestructure.database_controllers import DatabaseControllerPosgres

from domain.models import (
    DependencyInjection,
    Injection,
)

from domain.services.controllers import *
from domain.services.factories import *

class CoreBridge:
    def __init__(self):
        self.adapters = {
            "database_controller_postgres": DatabaseControllerPosgres(),
            "database_controller_factory_postgres": DatabaseControllerFactoryPostgres(),
        }
    
    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        return Injection(
            self.adapters[dependency_injection.database_controller],
            self.adapters[dependency_injection.database_controller_factory],
        )