import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Success!")
    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    create_connection(r"C:\sqlite\db\cinema.db")