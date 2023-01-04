from pathlib import Path
from app.checkers import check_n_tokens
from app.wrangling import clean_text
from constant import MODEL

BASE_DIR = Path(__file__).resolve(strict=True).parent


class Processing:
    def __init__(self, file: str):
        self.lines = None
        self.file = file

    def read(self) -> list:
        with open(self.file) as f:
            self.lines = f.readlines()
        return self.lines

    def embeddings(self):
        data = []
        lines = self.read()
        for line in lines:
            cleaned_line = clean_text(line)
            sentences = check_n_tokens(cleaned_line)
            data = data + sentences
        MODEL.encode(data)
        return MODEL

    def save_model(self):
        model = self.embeddings()
        model.save(str(BASE_DIR) + '/model')