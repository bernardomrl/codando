from dataclasses import dataclass

@dataclass
class DatabaseSettings:
    host: str
    port: int
    user: str
    password: str
    database_name: str