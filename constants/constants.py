import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # This is your Project Root
RESOURCE_DIR = os.path.join(ROOT_DIR, 'resource')
RAR_FILEPATH = os.path.join(RESOURCE_DIR, 'data.rar')
EXTRACTED_IMAGES = os.path.join(RESOURCE_DIR, 'extracted_images')
VALIDATION_IMAGES = os.path.join(RESOURCE_DIR, 'validation_images')
TEST_DATA = os.path.join(RESOURCE_DIR, 'test_data')
DATA_ZIP_LOCATION = os.path.join(RESOURCE_DIR, '/archive.zip')
KAGGLE_DATA_SET_NAME = 'xainano/handwrittenmathsymbols'
