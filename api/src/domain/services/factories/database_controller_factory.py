from domain.services.controllers import DatabaseController

class DatabaseControllerFactory:
    def call(self) -> DatabaseController:
        raise NotImplementedError()