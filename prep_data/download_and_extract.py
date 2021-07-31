import shutil

import patoolib as plib
import os
from constants.constants import RESOURCE_DIR, EXTRACTED_IMAGES, RAR_FILEPATH, DATA_ZIP_LOCATION, KAGGLE_DATA_SET_NAME
import kaggle


def download_and_extract_data():
    """
    Downloads data, unzips and places it in the correct folder
    :return:
    """
    if not os.path.exists(RAR_FILEPATH):
        print(f'downloading data to {RESOURCE_DIR}')
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(KAGGLE_DATA_SET_NAME, path=RESOURCE_DIR, unzip=True)
        if os.path.isdir(EXTRACTED_IMAGES):
            # First unzip creates an extracted_images folder that we don't need.
            # Next extraction call will create the extracted_images and contents we will use
            shutil.rmtree(EXTRACTED_IMAGES)


    print(f'extracting to {RESOURCE_DIR}')
    plib.extract_archive(RAR_FILEPATH, outdir=RESOURCE_DIR)
