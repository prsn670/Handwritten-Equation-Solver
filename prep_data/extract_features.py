import cv2
import matplotlib.pyplot as plt
from constants.constants import ROOT_DIR
def img_thing():
    # read the image file
    img = plt.imread(ROOT_DIR + '/resource/extracted_images/5/5_56.jpg')

    # invert image
    invert = cv2.bitwise_not(img)

    # print(invert)
    return invert
