import os
from pathlib import Path
from app.checkers import check_allowed_file
from app.processing import Processing

UPLOAD_FOLDER = '/app/data/'
BASE_DIR = Path(__file__).resolve(strict=True).parent
PATH_DIR = (str(BASE_DIR) + UPLOAD_FOLDER)
files = os.listdir(PATH_DIR)


def main():
    for file in files:
        if check_allowed_file(file):
            processing = Processing(PATH_DIR + file)
            processing.save_model()
        else:
            print('The file is not in .txt format')


if __name__ == "__main__":
    main()
