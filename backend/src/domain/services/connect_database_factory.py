from domain.models import DatabaseSettings
from domain.services import DatabaseControllerFactory

class ConnectDatabaseFactory:
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        raise NotImplementedError()