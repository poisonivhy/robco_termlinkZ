import os

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))

CREDENTIAL_STORAGE = os.path.join(BASE_DIR, "yummy.json")

DATA_STORAGE = os.path.join(BASE_DIR, "data.json")
