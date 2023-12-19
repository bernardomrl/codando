from domain.services import ConnectDatabaseFactory, DatabaseController
from domain.models import DatabaseSettings

class GetDatabaseController:
    def __init__(self, connect_database_factory: ConnectDatabaseFactory):
        self.connect_database_factory = connect_database_factory
    
    # Fluxo de execução
    def execute(self, database_settings: DatabaseSettings) -> DatabaseController:
        # database_connection_factory retorna uma database_controller_factory
        database_controller_factory = self.database_connection_factory.call(database_settings)

        # database_controller_factory retorna uma database_controller.
        database_controller = database_controller_factory.call()

        # O intuito dessa usecase é pegar o database_controller, por isso estamos retornando o mesmo.
        return database_controller 