from prep_data.download_and_extract import download_and_extract_data
from prep_data.extract_features import img_thing
from constants.constants import EXTRACT_LOCATION
import os


if __name__ == "__main__":
    if not os.path.isdir(EXTRACT_LOCATION + "/extracted_images"):
        download_and_extract_data()
    else:
        print('file already exists')

    img_thing()
