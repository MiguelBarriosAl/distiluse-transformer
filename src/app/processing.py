import time
from pathlib import Path
from app.checkers import check_n_tokens
from app.wrangling import clean_text
from sentence_transformers import SentenceTransformer, evaluation

BASE_DIR = Path(__file__).resolve(strict=True).parent


class Processing:
    def __init__(self, file: str):
        self.model = None
        self.lines = None
        self.file = file

    def read(self, file: str) -> list:
        with open(file) as f:
            self.lines = f.readlines()
        return self.lines

    def _clean_text(self, line: str) -> str:
        return clean_text(line)

    def embeddings(self):
        data = []
        lines = self.read(self.file)
        self.model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
        for line in lines:
            clean_line = self._clean_text(line)
            sentences = check_n_tokens(clean_line)
            data = data + sentences
        self.model.encode(data)
        return self.model

    def save_model(self):
        model = self.embeddings()
        model.save(str(BASE_DIR) + '/model')
