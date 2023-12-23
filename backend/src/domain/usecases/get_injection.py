from domain.services.factories import CoreDependecyInjectionFactory
from domain.services.bridges import CoreBridge

class GetInjection:
    def __init__(
        self,
        core_bridge: CoreBridge,
        core_dependency_injection_factory: CoreDependecyInjectionFactory,
    ):
        self.core_bridge = core_bridge
        self.core_dependency_injection_factory = (
            core_dependency_injection_factory
        )