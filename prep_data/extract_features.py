import cv2
import os
from constants.labels import test_label_dict
from prompt_toolkit.data_structures import Point

from constants.constants import EXTRACTED_IMAGES, TEST_DATA
from constants.labels import label_dict
from util.overlap import doOverlap


def extract_training_img_data(folder):
    """
    Processes the image for training. Making the image binary, creating bounding boxes around the features, and resizing.
    :param folder: folder where images reside
    :return:
    """
    train_data = []
    label_array = []
    folder_path = os.path.join(EXTRACTED_IMAGES, folder)
    for filename in os.listdir(folder_path):
        # read the image file
        # img = plt.imread(os.path.join(folder_path, filename))
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)

        # invert image pixels
        invert = cv2.bitwise_not(img)
        # make image binary (black or white) based on threshold value
        ret, thresh = cv2.threshold(invert, 127, 255, cv2.THRESH_BINARY)
        # Sort contours
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # sort contours form left to right
        sorted_bounding_boxes = sort_contours(contours)

        # resize contour regions to 28 x 28
        maxi = 0
        for box in sorted_bounding_boxes:
            # get top left corner point as well as width and height of box
            x, y, width, height = cv2.boundingRect(box)
            maxi = max(width * height, maxi)
            if maxi == width * height:
                x_max = x
                y_max = y
                w_max = width
                h_max = height

            # crop the bounding box(the contour) on the original inverted image
            crop_img = invert[y_max:y_max + h_max + 10, x_max:x_max + w_max + 10]
            # resize the cropped image and scale to a 28 x 28 image
            resize_img = cv2.resize(crop_img, (28, 28))
            train_data.append(resize_img)
            label_array.append(label_dict[folder])

    # used for verification
    # cv2.imwrite('invert_pic.jpg', invert)
    # print(invert)

    return train_data, label_array


def extract_test_img_data(img_name):
    """
    Processes the image for testing. Making the image binary, creating bounding boxes around the features, and resizing.
    Also tries to remove overlapping bounding boxes.
    :param img_name:
    :return:
    """
    img_data = []
    img_path = os.path.join(TEST_DATA, img_name)

    # read the image file
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # invert image
    invert = cv2.bitwise_not(img)
    ret, thresh = cv2.threshold(invert, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow("work", invert)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # get contours from image
    contours, ret = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Sort contours
    sorted_bounding_boxes = sort_contours(contours)
    # sort contours form left to right
    bounding_rects = []
    drop_rect = []

    # Remove multiple contours for the same digit. Drop smaller bounding rectangles.
    for box in sorted_bounding_boxes:
        # get top left corner point as well as width and height of box and put into a list
        x, y, w, h = cv2.boundingRect(box)
        rect = [x, y, w, h]
        bounding_rects.append(rect)  # returns - x, y, width, height
    for rect in bounding_rects:
        for rect_2 in bounding_rects:
            if rect == rect_2:
                continue
            else:
                # get coordinates for top-left and bottom-right of rectangle
                l1 = Point(rect[0], rect[1])
                r1 = Point(rect[0] + rect[2] + 10, rect[1] - rect[3] - 10)
                l2 = Point(rect_2[0], rect_2[1])
                r2 = Point(rect_2[0] + rect_2[2] + 10, rect_2[1] - rect_2[3] - 10)
                # check if rectangles overlap, with padding
                if doOverlap(l1, r1, l2, r2):
                    # check for smaller rectangle
                    area1 = rect[2] * rect[3]
                    area2 = rect_2[2] * rect_2[3]
                    if (area1 == min(area1, area2)):
                        drop_rect.append(rect)
                    else:
                        drop_rect.append(rect_2)
    # remove bounding rectangles from list
    for rect in drop_rect:
        try:
            bounding_rects.remove(rect)
        except ValueError:
            continue

    # crop the individual characters
    print(f'Number of characters seen by extractor for {img_name}: {len(bounding_rects)}')
    print(f'Number of actual characters in image {img_name}: {len(test_label_dict[img_name])}')
    for rect in bounding_rects:
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        crop_img = thresh[y:y + h + 10, x:x + w + 10]
        # resize the cropped image and scale to a 28 x 28 image
        resize_img = cv2.resize(crop_img, (28, 28))
        # cv2.imshow("work", resize_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        img_data.append(resize_img)

    return img_data


def sort_contours(ctrs):
    # construct the array of bounding boxes and sort them from left to right

    bounding_boxes = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    # return the list of sorted contours and bounding boxes
    return bounding_boxes
