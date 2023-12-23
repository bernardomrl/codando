from domain.models import DependencyInjection

class CoreDependecyInjectionFactory:
    def call(self) -> DependencyInjection:
        raise NotImplementedError()