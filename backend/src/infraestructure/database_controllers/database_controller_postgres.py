from domain.services.controllers import DatabaseController
import psycopg2 as psycopg

class DatabaseControllerPostgres(DatabaseController):
    def __init__(self, cursor: psycopg.cursor):
        self.cursor = cursor

    def execute(self, query: str, params: tuple[str] = (), isselect=True) -> list[str]:
        self.cursor.execute(query, params)

        if isselect:
            return list(self.cursor.fetchall())
        else:
            return []