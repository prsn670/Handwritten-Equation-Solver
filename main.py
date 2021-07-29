import numpy as np

from prep_data.download_and_extract import download_and_extract_data
from prep_data.extract_features import img_thing
from constants.constants import EXTRACTED_IMAGES, VALIDATION_IMAGES
from train_test_model.cnn_train import train_model
import os

if __name__ == "__main__":
    train_data = []
    train_labels = []
    validation_data = []
    validation_labels = []
    if not os.path.isdir(EXTRACTED_IMAGES):
        download_and_extract_data()
    else:
        print('file already exists')

    for folder in os.listdir(EXTRACTED_IMAGES):
        extracted_results = img_thing(folder)
        train_data.extend(extracted_results[0])
        train_labels.extend(extracted_results[1])

    for folder in os.listdir(VALIDATION_IMAGES):
        extracted_validation_results = img_thing(folder)
        validation_data.extend(extracted_validation_results[0])
        validation_labels.extend(extracted_validation_results[1])

    print(len(train_data), "Train sample size")
    print(len(train_data[0]), len(train_data[0][0]), "Train dimensions")
    print(len(validation_data), "Validation sample size")
    print(len(validation_data[0]), len(validation_data[0][0]), "Validation dimensions")
    # print(np.array(validation_labels).shape)
    # print(np.array(train_labels).shape)

    train_model(train_data, train_labels, validation_data, validation_labels)
    print("done")
