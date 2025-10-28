import csv
import sqlite3
from pathlib import Path
            
class SqliteWork:
    __pathDB = ""

    def __init__(self):
        __pathDB = ""

    def data_path(self, data_path):
        self.__pathDB = data_path
    
    def initialization_tables(self, connection):
        try:
            
            create_table_player = '''
            CREATE TABLE IF NOT EXISTS "player" (
                "player_id"	INTEGER NOT NULL,
                "nickname"	TEXT NOT NULL UNIQUE,
                "password"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("player_id" AUTOINCREMENT)
            );
            '''

            create_table_character = '''
            CREATE TABLE IF NOT EXISTS "character" (
                "character_id"	INTEGER NOT NULL,
                "player_id"	INTEGER,
                "character_name"	TEXT NOT NULL,
                "id_class"	INTEGER NOT NULL,
                "id_race"	INTEGER NOT NULL,
                "id_alignments"	INTEGER NOT NULL,
                "languages"	TEXT NOT NULL,
                "lvl"	INTEGER NOT NULL DEFAULT 1,
                "exp"	INTEGER NOT NULL DEFAULT 0,
                "str"	INTEGER NOT NULL DEFAULT 10,
                "dex"	INTEGER NOT NULL DEFAULT 10,
                "con"	INTEGER NOT NULL DEFAULT 10,
                "int"	INTEGER NOT NULL DEFAULT 10,
                "wis"	INTEGER NOT NULL DEFAULT 10,
                "cha"	INTEGER NOT NULL DEFAULT 10,
                PRIMARY KEY("character_id" AUTOINCREMENT),
                FOREIGN KEY("id_alignments") REFERENCES "alignments"("alignments_id") ON DELETE SET NULL,
                FOREIGN KEY("id_class") REFERENCES "class_catalog"("class_id") ON DELETE SET NULL,
                FOREIGN KEY("id_race") REFERENCES "race"("race_id") ON DELETE SET NULL
            );
            '''
            #
            create_table_class_catalog = '''
            CREATE TABLE IF NOT EXISTS "class_catalog" (
                "class_id"	INTEGER NOT NULL,
                "class_name"	TEXT NOT NULL UNIQUE,
                "diceHP"	TEXT NOT NULL,
                "startHP"	INTEGER NOT NULL,
                PRIMARY KEY("class_id" AUTOINCREMENT)
            );
            '''
            #
            create_table_race = '''
            CREATE TABLE IF NOT EXISTS "race" (
                "race_id"	INTEGER NOT NULL,
                "race_nameFirst"	TEXT NOT NULL,
                "race_nameSecond"	TEXT,
                "size"	TEXT NOT NULL,
                "speed"	TEXT NOT NULL,
                "strPlus"	INTEGER NOT NULL DEFAULT 0,
                "dexPlus"	INTEGER NOT NULL DEFAULT 0,
                "conPlus"	INTEGER NOT NULL DEFAULT 0,
                "intPlus"	INTEGER NOT NULL DEFAULT 0,
                "wisPlus"	INTEGER NOT NULL DEFAULT 0,
                "chaPlus"	INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY("race_id" AUTOINCREMENT)
            );
            '''
            #
            create_table_alignments ='''
            CREATE TABLE IF NOT EXISTS "alignments" (
                "alignments_id"	INTEGER NOT NULL,
                "alignments_name"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("alignments_id" AUTOINCREMENT)
            );
            '''
            #
            create_table_languages_catalog ='''
            CREATE TABLE IF NOT EXISTS "Languages_catalog" (
                "id_character"	INTEGER NOT NULL,
                "id_lBD"	INTEGER NOT NULL,
                PRIMARY KEY("id_character", "id_lBD"),
                FOREIGN KEY("id_character") REFERENCES "character"("character_id") ON DELETE CASCADE,
                FOREIGN KEY("id_lBD") REFERENCES "languages_BD"("languages_id") ON DELETE CASCADE
            );
            '''
            #
            create_table_language_BD = '''
            CREATE TABLE IF NOT EXISTS "languages_BD" (
                "languages_id"	INTEGER NOT NULL,
                "language_name"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("languages_id" AUTOINCREMENT)
            );
            '''
            #
            create_table_skills_BD = '''
            CREATE TABLE IF NOT EXISTS "skills_BD" (
                "Skill_id"	INTEGER NOT NULL,
                "skill_nameFirst"	TEXT NOT NULL,
                "description"	TEXT NOT NULL,
                "lvl_class"	INTEGER NOT NULL,
                "id_class"	INTEGER,
                "id_race"	INTEGER,
                PRIMARY KEY("Skill_id" AUTOINCREMENT),
                FOREIGN KEY("id_class") REFERENCES "class_catalog"("class_id") ON DELETE SET NULL,
                FOREIGN KEY("id_race") REFERENCES "race"("race_id") ON DELETE SET NULL
            );
            '''
            #
            create_table_SK_skills_BD = '''
            CREATE TABLE IF NOT EXISTS "SK_skills_BD" (
                "SK_skills_BD_id"	INTEGER NOT NULL,
                "SK_skill_name"	TEXT NOT NULL,
                "description"	TEXT NOT NULL,
                "id_skills_BD"	INTEGER NOT NULL,
                PRIMARY KEY("SK_skills_BD_id" AUTOINCREMENT),
                FOREIGN KEY("id_skills_BD") REFERENCES "skills_BD"("Skill_id") ON DELETE CASCADE
            );
            '''
            
            create_table_stats = '''
            CREATE TABLE "stats" (
                "stats_id"	INTEGER NOT NULL,
                "stats_str"	TEXT NOT NULL DEFAULT 10,
                "stats_dex"	TEXT NOT NULL DEFAULT 10,
                "stats_con"	INTEGER DEFAULT 10,
                "stats_int"	INTEGER NOT NULL DEFAULT 10,
                "stats_wis"	INTEGER NOT NULL DEFAULT 10,
                "stats_cha"	INTEGER NOT NULL DEFAULT 10,
                "id_character"	INTEGER UNIQUE,
                PRIMARY KEY("stats_id" AUTOINCREMENT),
                FOREIGN KEY("id_character") REFERENCES "character"("character_id") ON DELETE CASCADE
            );
            '''

            list_table = [
                create_table_player,
                create_table_character,
                create_table_class_catalog,
                create_table_race,
                create_table_alignments,
                create_table_languages_catalog,
                create_table_language_BD,
                create_table_skills_BD,
                create_table_SK_skills_BD,
                create_table_stats
            ]
            cursor = connection.cursor()
            print("SQLite is connected(initialization_tables)")
            for let in list_table:
                cursor.execute(let)

            connection.commit()
            print("Tables SQLite create(initialization_tables)")
            cursor.close()
        except sqlite3.Error as error:
            print("Error initialization_tables! Error: ", error)

    def initialization_fill(self, connection):
        try:
            list_BD = [
                "alignments",
                "character",
                "class_catalog",
                "languages_BD",
                "Languages_catalog",
                "player",
                "race",
                "SK_skills_BD",
                "skills_BD",
                "stats"
            ]

            root_dir = Path(__file__).absolute().parents[1]
            dirfile = f"{root_dir}\\Lib\\FilesDB\\"

            cursor = connection.cursor()

            for let_file in list_BD:
                with open(dirfile+let_file+".csv", "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cursor.execute(f"INSERT OR IGNORE INTO {let_file}{tuple(row)} VALUES {tuple(row.values())}")
            
            connection.commit()

            print("Fill tables SQLite is complited(initialization_tables)")
            cursor.close()
        except sqlite3.Error as error:
            print("Error initialization_fill! Error: ", error)

    def open_connection(self):
        try:
            connection = sqlite3.connect(self.__pathDB)
            #connection = sqlite3.connect('Base_Project/Lib/character.db')
            return connection
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite! Error: ", error)
            if (connection):
                connection.close()
                print("Sqlite connected close(open_connection)")

    def close_connection(connetion):
        if (connetion):
                connetion.close()
                print("Sqlite connected close(close_connection)")

    def get_character_from_BD(connection, name_character):
        try:
            get_character = f'''
            SELECT
                character.character_name,
                
                alignments.alignments_name,
                (SELECT GROUP_CONCAT(languages_BD.language_name, ',')
                    FROM Languages_catalog
                    JOIN languages_BD ON Languages_catalog.id_lBD = languages_BD.languages_id
                    WHERE Languages_catalog.id_character = character.character_id) as languages_BD,
                character.lvl,
                character.exp
            FROM character 
            
            JOIN alignments ON character.id_alignments = alignments.alignments_id
            WHERE character.character_name = '{name_character}'
            '''

            cursor = connection.cursor()
            cursor.execute(get_character)
            character = tuple(cursor.fetchall())[0]
            cursor.close()
            print("Complited get_character_from_BD!")
            return character
        except sqlite3.Error as error:
            print(f"Error get_character_from_BD! Error:", error)

    def get_character_race(connection, name_character):
        try:
            get_character_race = f'''
            SELECT
                race.race_nameFirst,
                race.race_nameSecond
            FROM character 
            JOIN race ON character.id_race = race.race_id
            WHERE character.character_name = '{name_character}'
            '''

            cursor = connection.cursor()
            cursor.execute(get_character_race)
            character_race = tuple(cursor.fetchall())[0]
            cursor.close()
            print("Complited get_character_race")
            return character_race
        except:
            print("Error get_character_race")

    def get_character_class(connection, name_character):
        try:
            get_character_class = f'''
                SELECT
                    class_catalog.class_name
                FROM character 
                JOIN class_catalog ON character.id_class = class_catalog.class_id
                WHERE character.character_name = '{name_character}'
                '''

            cursor = connection.cursor()
            cursor.execute(get_character_class)
            character_class = tuple(cursor.fetchall())[0]
            cursor.close()
            print("Complited get_character_race")
            return character_class
        except:
            print("Error get_character_race")

    def get_character_languages():
        pass

    def get_character_alignments():
        pass

    def get_character_stats(connection, name_character):
        try:
            get_stats = f'''
            SELECT
                stats.stats_str,
                stats.stats_dex, 
                stats.stats_con, 
                stats.stats_int,
                stats.stats_wis, 
                stats.stats_cha
            FROM character
            JOIN stats ON stats.id_character = character.character_id
            WHERE character.character_name = '{name_character}'
            '''
            cursor = connection.cursor()
            cursor.execute(get_stats)
            character_stats = tuple(cursor.fetchall())[0]
            cursor.close()
            print("Complited get_character_stats")
            return character_stats
        except:
            print("Error get_character_stats_plus")
            return 0

    def get_character_stats_plus(connection, name_character):
        try:
            get_stats_plus = f'''
            SELECT
                race.strPlus, 
                race.dexPlus, 
                race.conPlus,
                race.intPlus, 
                race.wisPlus,
                race.conPlus
            FROM character
            JOIN race ON race.race_id = character.id_race
            WHERE character.character_name = '{name_character}'
            '''
            cursor = connection.cursor()
            cursor.execute(get_stats_plus)
            character_stats_plus = tuple(cursor.fetchall())[0]
            cursor.close()
            print("Complited get_character_stats_plus")
            return character_stats_plus  
        except:
            print("Error get_character_stats_plus")
            return 0

SqliteWork.data_path(SqliteWork, 'Base_Project/Lib/DBApp.db')
connect = SqliteWork.open_connection(SqliteWork)
SqliteWork.initialization_tables(SqliteWork, connect)
SqliteWork.initialization_fill(SqliteWork, connect)
character = SqliteWork.get_character_from_BD(connect, "Jhon")
print(character)
char_race = SqliteWork.get_character_race(connect, "Jhon")
print(char_race)
char_class = SqliteWork.get_character_class(connect, "Jhon")
print(char_class)
test1 = SqliteWork.get_character_stats(connect, "Jhon")
print(test1)
test2 = SqliteWork.get_character_stats_plus(connect, "Jhon")
print(test2)
SqliteWork.close_connection(connect)