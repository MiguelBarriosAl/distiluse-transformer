from app.checkers import check_allowed_file
from app.processing import Processing
from constant import FILES, PATH_DIR


def main():
    for file in FILES:
        if check_allowed_file(file):
            processing = Processing(PATH_DIR + file)
            processing.save_model()
        else:
            print('The file is not in .txt format')


if __name__ == "__main__":
    main()
