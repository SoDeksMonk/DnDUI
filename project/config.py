from pathlib import Path
import configparser
#import os, sys

config = configparser.ConfigParser()
config.read("setting.ini")

HOME_DIR = Path(__file__).resolve().parents[1]

PROJECT_DIR = HOME_DIR / "project"
DATA_DIR = PROJECT_DIR / "data"
DATABASE_DIR = DATA_DIR / "database"
RESERVE_DIR = DATABASE_DIR / "reserve"

FRONT_DIR = DATA_DIR / "front"
IMAGE_DIR = FRONT_DIR / "image"

LOCALIZATION_DIR = DATA_DIR / "localization"


#sys.path.append(os.path.dirname(HOME_DIR))
#sys.path.append(os.path.dirname(PROJECT_DIR))
#sys.path.append(os.path.dirname(DATA_DIR))
#sys.path.append(os.path.dirname(DATABASE_DIR))
#sys.path.append(os.path.dirname(RESERVE_DIR))
#sys.path.append(os.path.dirname(FRONT_DIR))
#sys.path.append(os.path.dirname(IMAGE_DIR))
#sys.path.append(os.path.dirname(LOCALIZATION_DIR))



