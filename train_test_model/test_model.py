import os
import numpy as np
from keras.models import model_from_json
from prep_data.extract_features import extract_test_img_data
from constants.labels import label_dict, test_label_dict
from constants.constants import TEST_DATA


def test_model():
    json_file = open('model_final.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('best.hdf5')
    # print(loaded_model.get_weights())
    correct = 0
    for file_name in os.listdir(TEST_DATA):
        test_data = extract_test_img_data(file_name)

        # list out keys and values separately
        key_list = list(label_dict.keys())
        val_list = list(label_dict.values())

        result_string = ''
        for data in test_data:
            evaluate_data = np.array(data)
            evaluate_data = data.reshape(1, evaluate_data.shape[0], evaluate_data.shape[1], 1)
            result = loaded_model.predict_classes(evaluate_data)
            value_position = val_list.index(str(result[0]))
            key = key_list[value_position]
            result_string += str(key)
            if result_string == test_label_dict[file_name]:
                print('Match')
                correct += 1
                print(f'Resulting string evaluates to: {eval(result_string)}')
        print(f'model equation result: {result_string}')
        print(f'actual equation: {test_label_dict[file_name]}\n')


    print(f'Correct number of guesses: {correct} out of {len(os.listdir(TEST_DATA))}')
