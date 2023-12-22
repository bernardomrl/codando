from domain.services.factories import DatabaseConnectionFactory
from domain.services.controllers import DatabaseController
from domain.models import DatabaseSettings

class GetDatabaseController:
    def __init__(self, database_connection_factory: DatabaseConnectionFactory):
        self.database_connection_factory = database_connection_factory

    def call(self, database_settings: DatabaseSettings) -> DatabaseController:
        database_controller_factory = self.database_connection_factory.call(database_settings)
        return database_controller_factory.call()