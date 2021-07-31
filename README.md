# Handwritten-Equation-Solver
Takes in a handwritten equation predicts the characters and outputs the result. Note that the eval method is currently commented out. 

## Running the project
Python 3.8 was used in the making of this project with Anaconda. Program was run in Pycharm 2021.1.3. Using the run button in main.py with configuration to run in Python console enabled. You may also run this program from the terminal. Go to the root directory of the project (Handwritten-Equation-Solver) and use `python main.py` to run. Make sure you install the needed packages listed below before running.
### Install
Install the following packages:
- pip install patool (for extracting rar)
- pip install opencv-python
    - opencv_version = "4.5.3.56"
- pip install pillow (to read jpg file)
- pip install kaggle (used to download dataset)
    - instructions for setting up kaggle api used for downloading data set https://adityashrm21.github.io/Setting-Up-Kaggle/
    - I have provided a small subset of the data used in this project, but for best results, using the all provided data is best. You can either let the program download it for you or do this manually. To start the downloading and extraction of data, delete the current extracted_images folder. Keep in mind this is a large file, we're not using all the classes, it may be easier to download this manually (below).
    
### Manually Downloading Data
- Sample data is from https://www.kaggle.com/xainano/handwrittenmathsymbols
- The above will download and archive.zip file. Unzip the file.
- Contents of the zipped file will have a data.rar and extracted_images file. Delete the extracted_images file and then extract data.rar. This will create a new extracted_images file with all the data.
- We're only using +, -, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 folders in this project
- Place the above folders in its own extracted_images folder and place extracted_images in the resource folder of the project.

### File Descriptions
- main.py - entry point of program and orchestrates the calls along with some logic that bypasses function calls based on what files/folders are currently in the project
- constants - directory containing constants
    - constants.py - contains constants for file and directory paths
    - labels.py - contains dictionary mapping characters to classes and the expected strings that are to be produces from the test data
- prep_data - responsible for downloading, extracting features, and splitting data into training and validation folders
    - download_and_extract.py - downloads and unzips the data while placing it in the correct location for the project. Only executes if the extracted_images file does not exist. (see above notes about installation instructions and manually downloading data)
    - extract_features.py - finds contours of the data and places bounding boxes around the image for training and testing
    - split_data.py - takes data from extracted_images and creates a validation_images folder, placing half of the data from extracted_images
- resource - contains resources used in train, validation, and testing of model
    - extracted_images - Contains images used in training data
    - test_data - Contains images used in testing data
    - validation_images - created during split_data function. Contains images used for validation
- train_test_model - files used to train and test model
    - cnn_train.py - trains the model, validates, and chooses the best outcome based on accuracy while keeping track of loss
    - test_model.py - tests the model, prints out the predicted and expected(actual) resulting string
- util
    - overlap.py - used to determine if two bounding boxes overlap. If so, the one with a smaller area is chosen.
- model_final.json - contains the model information. Used to load the model into test_model.py
- best.hdf5 - contains the best weights determined during the training process



### References
These sites helped in researching and preparing this project. Discussion and code are available to learn from. 
- https://www.pyimagesearch.com/2020/08/24/ocr-handwriting-recognition-with-opencv-keras-and-tensorflow/
- https://vipul-gupta73921.medium.com/handwritten-equation-solver-using-convolutional-neural-network-a44acc0bd9f8
- https://github.com/vipul79321/Handwritten-Equation-Solver
- https://github.com/udacity/machine-learning/blob/master/projects/practice_projects/cnn/mnist-mlp/mnist_mlp.ipynb
- https://github.com/udacity/machine-learning/blob/master/projects/practice_projects/cnn/cifar10-classification/cifar10_cnn.ipynb

