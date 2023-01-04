import re


def clean_text(text: str) -> str:
    body = re.sub(r"[^a-zA-Za-z0-9.,!?]", ' ', text)
    return body.strip()


def split_text(text: str, n: int) -> list:
    n_splits = n//512
    rs_text = text.rsplit(".", n_splits)
    if len(rs_text) < 2:
        return text.rsplit(",", n_splits)
    return rs_text

