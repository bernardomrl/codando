from domain.services.factories import CoreDependencyInjectionFactory
from domain.models import DependencyInjection
import json, os

class CoreDependencyInjectionFactoryJson(CoreDependencyInjectionFactory):
    def call(self) -> DependencyInjection:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(current_dir, "utils", "dependency_injections.json")

        with open(json_path) as file:
            dependency_injections = json.load(file)
            return DependencyInjection(
                dependency_injections["database_connection_factory"],
                dependency_injections["database_controller_factory"],
                dependency_injections["database_controller"],
            )