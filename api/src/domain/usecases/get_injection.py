from domain.services.factories import CoreDependencyInjectionFactory
from domain.services.bridges import CoreBridge
from domain.models import Injection

class GetInjection:
    def __init__(
        self,
        core_dependency_injection_factory: CoreDependencyInjectionFactory,
        core_bridge: CoreBridge,
    ) -> None:
        self.core_dependency_injection_factory = core_dependency_injection_factory
        self.core_bridge = core_bridge

    def call(self) -> Injection:
        dependency_injection = self.core_dependency_injection_factory.call()
        return self.core_bridge.get_injection(dependency_injection)