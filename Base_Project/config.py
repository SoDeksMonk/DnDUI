from pathlib import Path
import configparser
import os, sys

config = configparser.ConfigParser()
config.read("setting.ini")

HOME_DIR = Path(__file__).resolve()

BASE_PROJECT_DIR = HOME_DIR / "Base_Project"
FRONT_DIR = BASE_PROJECT_DIR / "Front"

LIB_DIR = BASE_PROJECT_DIR / "Lib" 
FILESDB_DIR = LIB_DIR / "FilesDB"

MAIN_DIR = BASE_PROJECT_DIR / "Main"

sys.path.append(os.path.dirname(HOME_DIR))
sys.path.append(os.path.dirname(BASE_PROJECT_DIR))
sys.path.append(os.path.dirname(FRONT_DIR))
sys.path.append(os.path.dirname(LIB_DIR))
sys.path.append(os.path.dirname(FILESDB_DIR))
sys.path.append(os.path.dirname(MAIN_DIR))



