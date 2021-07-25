import cv2
import matplotlib.pyplot as plt
from constants.constants import ROOT_DIR


def img_thing():
    train_data = []
    # read the image file
    img = plt.imread(ROOT_DIR + '/resource/extracted_images/5/5_56.jpg')

    # invert image
    invert = cv2.bitwise_not(img)
    # Sort contours
    contours, hierarchy = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # sort contours form left to right
    sorted_bounding_boxes = sort_contours(contours)

    # resize bounding boxes to 28 x 28
    maxi = 0
    for box in sorted_bounding_boxes:
        # get top right corner point as well as width and height of box
        x, y, width, height = cv2.boundingRect(box)
        maxi = max(width * height, maxi)
        if maxi == width * height:
            x_max = x
            y_max = y
            w_max = width
            h_max = height

        # crop the bounding box(the contour) on the original inverted image
        crop_img = invert[y_max:y_max+h_max+10, x_max:x_max+w_max+10]
        # resize the cropped image and scale to a 28 x 28 image
        resize_img = cv2.resize(crop_img, (28, 28))
        train_data.append(resize_img)


    # used for verification
    # cv2.imwrite('invert_pic.jpg', invert)
    # print(invert)

    return train_data


def sort_contours(ctrs):
    # construct the array of bounding boxes and sort them from left to right

    bounding_boxes = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    # return the list of sorted contours and bounding boxes
    return bounding_boxes