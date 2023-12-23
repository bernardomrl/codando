from domain.models import DependencyInjection, Injection

class CoreBridge:
    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        raise NotImplementedError()