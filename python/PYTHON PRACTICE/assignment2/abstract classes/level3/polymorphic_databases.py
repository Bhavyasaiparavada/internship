from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL database."


class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL database."


class MongoDatabase(Database):
    def connect(self):
        return "Connected to MongoDB database."


databases = [MySQLDatabase(), PostgreSQLDatabase(), MongoDatabase()]
for database in databases:
    print(database.connect())
