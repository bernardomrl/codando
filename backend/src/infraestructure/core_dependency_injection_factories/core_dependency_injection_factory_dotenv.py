from domain.services.factories import CoreDependecyInjectionFactory
from domain.models import DependencyInjection, DatabaseSettings
from dotenv import load_dotenv
import os

class CoreDependecyInjectionFactoryDotEnv(CoreDependecyInjectionFactory):
    def __init__(self):
        load_dotenv("database_settings.py")

    def call(self) -> DependencyInjection:
        dependency_injections = {
            
        }