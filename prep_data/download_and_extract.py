import shutil

import patoolib as plib
import os
from constants.constants import EXTRACT_LOCATION, RAR_FILEPATH, DATA_ZIP_LOCATION, KAGGLE_DATA_SET_NAME
import kaggle


def download_and_extract_data():
    if not os.path.exists(RAR_FILEPATH):
        print(f'downloading data to {EXTRACT_LOCATION}')
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(KAGGLE_DATA_SET_NAME, path=EXTRACT_LOCATION, unzip=True)
        if os.path.isdir(EXTRACT_LOCATION + "\\extracted_images"):
            # First unzip creates an extracted_images folder that we don't need.
            # Next extraction call will create the extracted_images and contents we will use
            shutil.rmtree(EXTRACT_LOCATION + "\\extracted_images")


    print(f'extracting to {EXTRACT_LOCATION}')
    plib.extract_archive(RAR_FILEPATH, outdir=EXTRACT_LOCATION)
