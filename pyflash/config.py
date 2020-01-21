import os
import configparser

config = configparser.ConfigParser()

config_path = os.path.dirname(os.path.abspath(__file__)) + "/../setup.cfg"

config.read(config_path)

games_dir = config.get("general", "games_folder")
