from domain.services.factories import DatabaseControllerFactory
from domain.models import DatabaseSettings

class DatabaseConnectionFactory:
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        raise NotImplementedError()