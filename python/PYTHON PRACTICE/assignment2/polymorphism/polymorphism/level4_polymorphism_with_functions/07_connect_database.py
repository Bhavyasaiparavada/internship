class MySQL:
    def connect(self):
        print("Connected to MySQL")


class SQLite:
    def connect(self):
        print("Connected to SQLite")


def connect_database(database):
    database.connect()


connect_database(MySQL())
connect_database(SQLite())