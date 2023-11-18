from sqlalchemy import MetaData, create_engine
from configparser import ConfigParser
import os

env = os.getenv("ENV", ".config")

if env == ".config":
    config = ConfigParser()
    config.read(".config")
    config = config["MYSQL"]
else:
    config = {
        "CONNECTION": os.getenv("CONNECTION", "your.domain.com"),
    }

engine = create_engine(config["CONNECTION"])

meta_data = MetaData()