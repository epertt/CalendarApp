import os
from dotenv import dotenv_values

root_directory = os.path.join(os.path.dirname(__file__), "..")
env_file_path = os.path.join(root_directory, ".env")

if os.path.isfile(env_file_path):
    config = dotenv_values(dotenv_path=env_file_path)
else:
    with open(env_file_path, "w", encoding='UTF-8') as file:
        file.write("DB_FILE_NAME=db.sqlite")
        file.close()
    config = dotenv_values(dotenv_path=env_file_path)

DB_FILE_NAME = config["DB_FILE_NAME"] or "db.sqlite"
DB_FILE_PATH = os.path.join(root_directory, DB_FILE_NAME)
