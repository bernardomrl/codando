from domain.services.controllers import *
from domain.services.factories import *
from dataclasses import dataclass

@dataclass
class Injection:
    database_controller: DatabaseController
    database_controller_factory: DatabaseControllerFactory