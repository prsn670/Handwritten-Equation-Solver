import numpy as np
from keras.models import model_from_json
from prep_data.extract_features import extract_test_img_data
from constants.labels import label_dict


def test_model():
    json_file = open('model_final.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights('best.hdf5')
    # print(loaded_model.get_weights())
    # extract test img
    test_data = extract_test_img_data('test3.jpg')
    # print(len(test_data))
    # print(len(test_data[0]))
    # print(len(test_data[0][0]))

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
    print(f'{result_string} equals')
    print(eval(result_string))
