from pathlib import Path

from dotenv import load_dotenv
import os


load_dotenv(Path('../.env'))
env = os.environ


print(env)