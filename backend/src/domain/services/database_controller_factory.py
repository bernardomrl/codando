from domain.models import DatabaseSettings
from domain.services import DatabaseController

class DatabaseControllerFactory:
    def call(self, database_settings: DatabaseSettings) -> DatabaseController:
        raise NotImplementedError()