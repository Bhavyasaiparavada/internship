from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self, record):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")

    def insert(self, record):
        print("Inserted into MySQL:", record)

    def close(self):
        print("MySQL connection closed")


class SQLite(Database):
    def connect(self):
        print("Connected to SQLite")

    def insert(self, record):
        print("Inserted into SQLite:", record)

    def close(self):
        print("SQLite connection closed")


mysql = MySQL()
sqlite = SQLite()
mysql.connect()
mysql.insert("Asha")
mysql.close()
sqlite.connect()
sqlite.insert("Asha")
sqlite.close()