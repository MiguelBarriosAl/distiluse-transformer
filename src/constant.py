import os
from pathlib import Path
from sentence_transformers import SentenceTransformer

# List Files
upload_folder = '/app/data/'
base_dir = Path(__file__).resolve(strict=True).parent
PATH_DIR = (str(base_dir) + upload_folder)
FILES = os.listdir(PATH_DIR)

# Model
MODEL = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
