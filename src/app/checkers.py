from nltk.tokenize import word_tokenize
from app.wrangling import split_text

ALLOWED_EXTENSIONS = {'txt'}


def check_allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def n_tokens(text: str) -> int:
    return len(word_tokenize(text))


def check_n_tokens(text: str) -> list:
    tokens = n_tokens(text)
    if 50 <= tokens <= 512:
        text = [text]
    elif tokens > 512:
        text = split_text(text, tokens)
    elif tokens < 50:
        text = []
    return text



