import os
import shutil
import random as rand
from constants.constants import EXTRACTED_IMAGES, VALIDATION_IMAGES


def split_data():
    """
    Splits data into training and validation sections for training.
    :return:
    """
    # check if validation folder exists, create if not
    if not os.path.exists(VALIDATION_IMAGES):
        os.mkdir(VALIDATION_IMAGES)

    for folder in os.listdir(EXTRACTED_IMAGES):
        source_dir = os.path.join(EXTRACTED_IMAGES, folder)
        destination_dir = os.path.join(VALIDATION_IMAGES, folder)
        # check if folder for images exists, create if not
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
        for file_name in os.listdir(source_dir):
            # decide whether or not to add a file to our validation folder. Try and get a 50/50 split
            if len(os.listdir(source_dir)) <= len(os.listdir(destination_dir)):
                break

            if bool(rand.getrandbits(1)):
                shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, file_name))
