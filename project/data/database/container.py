import csv
import os
import sqlite3
from pathlib import Path
import logging
           
class SqliteWork:
    def __init__(self):
        self._pathDB = ""
    @classmethod
    def data_path(self, data_path):
        self._pathDB = data_path
    
    @classmethod
    def initialization_fill(self, connection:str ) -> None:
        try:
            root_dir = Path(__file__).absolute().parents[2]
            dirfile = f"{root_dir}\\data\\database\\reserve\\"

            cursor = connection.cursor()

            files = os.listdir(dirfile)
            for let_file in files:
                with open(dirfile +"\\"+let_file, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cursor.execute(
                            f"INSERT OR IGNORE INTO {let_file[:-4]}{tuple(row)}"
                            f" VALUES {tuple(row.values())}"
                            )
            
            connection.commit()

            logging.debug("Fill tables SQLite is complited(initialization_tables)")
            cursor.close()
        except sqlite3.Error as error:
            print("Error initialization_fill! Error: ", error)

    @classmethod
    def open_connection(self):
        try:
            connection = sqlite3.connect(self._pathDB)
            logging.debug("connection to the database is successful(open_connection)")
            return connection
        except sqlite3.Error as error:
            print("Error when connecting to sqlite! Error: ", error)
            if (connection):
                connection.close()
                
    @staticmethod
    def close_connection(connetion):
        if (connetion):
            connetion.close()
        logging.debug("Сonnection completed")