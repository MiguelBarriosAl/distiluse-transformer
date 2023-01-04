from nltk.tokenize import word_tokenize
from src.app.wrangling import split_text

ALLOWED_EXTENSIONS = {'txt'}


def check_allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def n_tokens(text: str) -> int:
    return len(word_tokenize(text))


def check_n_tokens(text: str) -> list:
    tokens = n_tokens(text)
    if 50 <= tokens <= 512:
        return [text]
    elif tokens > 512:
        return split_text(text, tokens)
    elif tokens < 50:
        return []



