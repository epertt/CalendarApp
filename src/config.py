import os
from dotenv import dotenv_values

root_directory = os.path.join(os.path.dirname(__file__), "..")
env_file_path = os.path.join(root_directory, ".env")

# dotenv_load and dotenv_values seem to never fail even if .env doesn't exist...
if os.path.isfile(env_file_path):
    config = dotenv_values(dotenv_path=env_file_path)
else:
    raise FileNotFoundError(f"no file found at {env_file_path}")

DB_FILE_NAME = config["DB_FILE_NAME"] or "db.sqlite"
DB_FILE_PATH = os.path.join(root_directory, DB_FILE_NAME)
