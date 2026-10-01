from abc import ABC, abstractmethod


class Database(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        return "Database: " + self.name


class MySQLDatabase(Database):
    def connect(self):
        return "Connected to database."


database = MySQLDatabase("MySQL")
print(database.display_database_name())
print(database.connect())