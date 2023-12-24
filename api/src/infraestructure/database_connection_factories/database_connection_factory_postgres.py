from infraestructure.database_controller_factories import DatabaseControllerFactoryPostgres
from domain.models import DatabaseSettings
from domain.services.factories import (
    DatabaseConnectionFactory,
    DatabaseControllerFactory
)

import psycopg2 as psycopg

class DatabaseConnectionFactoryPostgres(DatabaseConnectionFactory):
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        connection = psycopg.connect(
            host=database_settings.host,
            port=database_settings.port,
            user=database_settings.user,
            password=database_settings.password,
            dbname=database_settings.database_name,
        )

        return DatabaseControllerFactoryPostgres(connection)