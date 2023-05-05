import os
from os.path import join, dirname
from dotenv import load_dotenv

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path, override=True)

DEEPL_API_KEY = os.environ.get('DEEPL_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')