import time
from pathlib import Path
from src.app.checkers import check_n_tokens
from src.app.wrangling import clean_text
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve(strict=True).parent


class Processing:
    def __init__(self, file: str):
        self.file = file

    def read_txt(self):
        with open(self.file) as f:
            self.lines = f.readlines()
        return self.lines

    def _tokenizer(self, line):
        return clean_text(line)

    def embeddings(self):
        lines = self.read_txt()
        model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
        init = time.process_time()
        for line in lines[:10]:
            clean_line = self._tokenizer(line)
            sentences = check_n_tokens(clean_line)
            model.encode(sentences)
        model.save(str(BASE_DIR) + '/model')
        end = time.process_time()
        print(end - init)
