from nltk.tokenize import word_tokenize
from src.app.wrangling import split_text

ALLOWED_EXTENSIONS = {'txt'}


def check_allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_n_tokens(text: str) -> list:
    n_tokens = len(word_tokenize(text))
    if 50 <= n_tokens <= 512:
        text = [text]
    elif n_tokens > 512:
        text = split_text(text, n_tokens)
    elif n_tokens < 50:
        text = []
    return text
