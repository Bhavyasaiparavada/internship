import sqlite3

connection = None
try:
    connection = sqlite3.connect(":memory:")
    print("Connected to the SQLite database.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")