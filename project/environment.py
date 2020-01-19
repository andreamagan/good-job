import os
from environs import Env

env = Env()

# Load .env file from root folder
env.read_env(os.getcwd() + '/.env')