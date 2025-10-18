"""
import sqlite3

try:
    sqlite_connection = sqlite3.connect('Base_Project/Lib/character.db')
    sqlite_create_table_query = '''CREATE TABLE Race (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                speed TEXT NOT NULL);'''
    

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    cursor.execute('''DELETE TABLE sqlitedb_developers''')
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        """