from prep_data.extract import extract_data
from constants.constants import FILEPATH, EXTRACT_LOCATION
import os


if __name__ == "__main__":
    if not os.path.isdir(EXTRACT_LOCATION + "\\extracted_images"):
        print(f'extracting data files from {FILEPATH}')
        extract_data(FILEPATH)
    else:
        print('file already exists')

