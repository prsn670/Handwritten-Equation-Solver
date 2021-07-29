import keras.utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import keras.utils
import numpy as np
from keras.callbacks import ModelCheckpoint


def train_model(train_data, train_labels, validation_data, validation_labels):
    # Create training data
    num_classes = len(np.unique(train_labels))
    validation_classes = len(np.unique(validation_labels))
    print(validation_classes)
    x_train = np.array(train_data).reshape(62512, 28, 28, 1)
    y_train = keras.utils.to_categorical(train_labels, num_classes)
    x_validation = np.array(validation_data).reshape(62512, 28, 28, 1)
    y_validation = keras.utils.to_categorical(validation_labels, validation_classes)
    print(y_train.shape, "y_train shape")
    print(x_train.shape, "x_train shape")

    # Define the Model Architecture

    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=2, padding='same', activation='relu',
                     input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(500, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(12, activation='softmax'))

    print(model.summary())

    # compile the model
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop',
                  metrics=['accuracy'])

    # train the model
    checkpointer = ModelCheckpoint(filepath='best.hdf5', verbose=1,
                                   save_best_only=True)
    model.fit(x_train, y_train, batch_size=32, epochs=100,
              validation_data=(x_validation, y_validation), verbose=2,
              callbacks=[checkpointer], shuffle=True)
