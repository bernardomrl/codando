from infraestructure.database_controllers import DatabaseControllerPostgres
from domain.services.factories import DatabaseControllerFactory
from domain.services.controllers import DatabaseController
import psycopg2 as psycopg

class DatabaseControllerFactoryPostgres(DatabaseControllerFactory):
    def __init__(self, connection: psycopg.connect):
        self.connection = connection

    def call(self) -> DatabaseController:
        cursor = self.connection.cursor()
        return DatabaseControllerPostgres(cursor)