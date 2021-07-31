from prep_data.download_and_extract import download_and_extract_data
from prep_data.extract_features import extract_training_img_data
import time

from prep_data.split_data import split_data
from constants.constants import EXTRACTED_IMAGES, VALIDATION_IMAGES
from train_test_model.cnn_train import train_model
from train_test_model.test_model import test_model
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

    # perform data feature extraction and training only if file for model and weights hasn't been generated
    if not (os.path.isfile('best.hdf5') and os.path.isfile('model_final.json')):
        print("Creating training and validation data")
        start = time.time()
        split_data()
        end = time.time()
        print(end - start, "split data execution time")

        for folder in os.listdir(EXTRACTED_IMAGES):
            extracted_results = extract_training_img_data(folder)
            train_data.extend(extracted_results[0])
            train_labels.extend(extracted_results[1])

        for folder in os.listdir(VALIDATION_IMAGES):
            extracted_validation_results = extract_training_img_data(folder)
            validation_data.extend(extracted_validation_results[0])
            validation_labels.extend(extracted_validation_results[1])

        print(len(train_data), "Train sample size")
        print(len(train_data[0]), len(train_data[0][0]), "Train dimensions")
        print(len(validation_data), "Validation sample size")
        print(len(validation_data[0]), len(validation_data[0][0]), "Validation dimensions")
        # print(np.array(validation_labels).shape)
        # print(np.array(train_labels).shape)

        print("start training model")
        start = time.time()
        train_model(train_data, train_labels, validation_data, validation_labels)
        end = time.time()
        print(end - start, "train model execution time")
    test_model()
    print("done")
