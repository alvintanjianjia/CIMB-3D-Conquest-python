import numpy as np
import cv2
import csv
import math
from math import atan2, degrees
import tensorflow as tf
from functions import *





def getScanFormDetails(path, name=None):
    currentImage = cv2.imread(path)

    scale_percent = 50  # percent of original size
    width = int(currentImage.shape[1] * scale_percent / 100)
    height = int(currentImage.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    currentImage = cv2.resize(currentImage, dim, interpolation=cv2.INTER_AREA)
    print('Original Dimensions : ', currentImage.shape)
    # y first then x
    imgArray = []

    # First crop Student_ID number
    crop_img_1 = currentImage[260:290, 395:690]
    imgArray.append(crop_img_1)



    # Second crop Last_Name
    crop_img_2 = currentImage[285:320, 150:365]
    imgArray.append(crop_img_2)
    cv2.imwrite('test_word.jpg', crop_img_2)

    # Third crop First_Name
    crop_img_3 = currentImage[291:320, 470:700]
    imgArray.append(crop_img_3)

    # Fourth crop Course_Name
    crop_img_4 = currentImage[327:350, 170:700]
    imgArray.append(crop_img_4)

    # Fifth crop unit code
    crop_img_5 = currentImage[407:430, 135:250]
    imgArray.append(crop_img_5)

    # Sixth crop semester
    # crop_img_6 = currentImage[405:425, 370:400]
    # imgArray.append(crop_img_6)

    # Seventh crop year
    crop_img_7 = currentImage[400:425, 605:730]
    imgArray.append(crop_img_7)

    # Eighth crop unit title
    crop_img_8 = currentImage[430:455, 130:720]
    imgArray.append(crop_img_8)

    # Ninth crop c1
    crop_img_9 = currentImage[530:550, 77:720]
    imgArray.append(crop_img_9)

    # Tenth crop c2
    crop_img_10 = currentImage[555:575, 77:720]
    imgArray.append(crop_img_10)

    # Eleventh crop c3
    crop_img_11 = currentImage[580:600, 78:720]
    imgArray.append(crop_img_11)

    # Twelve crop c4
    crop_img_12 = currentImage[603:624, 77:720]
    imgArray.append(crop_img_12)

    # Thirteen crop c5
    crop_img_13 = currentImage[625:647, 77:720]
    imgArray.append(crop_img_13)

    # Fourteen crop c5
    crop_img_14 = currentImage[625:647, 77:720]
    imgArray.append(crop_img_14)

    # Fifteen crop C001
    crop_img_15 = currentImage[765:790, 77:310]
    imgArray.append(crop_img_15)

    # Sixteen crop C002
    crop_img_16 = currentImage[800:825, 77:310]
    imgArray.append(crop_img_16)

    # Seventeen crop Date 1
    crop_img_17 = currentImage[760:780, 580:740]
    imgArray.append(crop_img_17)

    # Eighteen crop Date 2
    crop_img_18 = currentImage[795:820, 580:740]
    imgArray.append(crop_img_18)

    # Initialise width and height for final picture
    max_width = 0
    total_height = 0


    ############ Get all information from current form #########################################
    for img in imgArray:
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]

    final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)
    alphabet_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)

    current_y = 0
    # keep track of current image placing in terms of Y coordinate
    for img in imgArray:
        final_image[current_y:img.shape[0] + current_y, :img.shape[1], :] = img
        current_y += img.shape[0]

    cv2.imshow('original_img', final_image)
    cv2.waitKey()



    ################## Get individual characters from current form ###############################
    # (h, w) = final_image.shape[:2]
    # image_size = h*w
    # mser = cv2.MSER_create()
    # mser.setMaxArea(image_size//2)
    # mser.setMinArea(40)

    # gray = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)  # Converting to GrayScale
    # _, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # regions, rects = mser.detectRegions(bw)
    # contours, hierarchy = cv2.findContours(final_image)

    # for (x,y,w,h) in rects:
    #     cv2.rectangle(final_image, (x, y), (x+w, y+h), color=(255, 0, 255), thickness = 1)

    # cv2.imshow('alphabet', final_image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()




def getScanFormDetails2(path, name=None):
    currentImage = cv2.imread(path)

    scale_percent = 50  # percent of original size
    width = int(currentImage.shape[1] * scale_percent / 100)
    height = int(currentImage.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    currentImage = cv2.resize(currentImage, dim, interpolation=cv2.INTER_AREA)
    print('Original Dimensions : ', currentImage.shape)
    # y first then x
    imgArray = []

    # First crop Student_ID number
    crop_img_1 = currentImage[250:280, 395:690]
    imgArray.append(crop_img_1)

    # Second crop Last_Name
    crop_img_2 = currentImage[275:310, 150:365]
    imgArray.append(crop_img_2)
    cv2.imwrite('test_word.jpg', crop_img_2)

    # Third crop First_Name
    crop_img_3 = currentImage[281:310, 470:700]
    imgArray.append(crop_img_3)

    # Fourth crop Course_Name
    crop_img_4 = currentImage[317:345, 170:700]
    imgArray.append(crop_img_4)

    # Fifth crop unit code
    crop_img_5 = currentImage[390:420, 135:250]
    imgArray.append(crop_img_5)

    # Sixth crop semester
    # crop_img_6 = currentImage[405:425, 370:400]
    # imgArray.append(crop_img_6)

    # Seventh crop year
    crop_img_7 = currentImage[390:415, 605:730]
    imgArray.append(crop_img_7)

    # Eighth crop unit title
    crop_img_8 = currentImage[420:445, 130:720]
    imgArray.append(crop_img_8)

    # Ninth crop c1
    crop_img_9 = currentImage[520:540, 77:750]
    imgArray.append(crop_img_9)

    # Tenth crop c2
    # crop_img_10 = currentImage[555:575, 77:720]
    # imgArray.append(crop_img_10)

    # Eleventh crop c3
    # crop_img_11 = currentImage[580:600, 78:720]
    # imgArray.append(crop_img_11)

    # Twelve crop c4
    # crop_img_12 = currentImage[603:624, 77:720]
    # imgArray.append(crop_img_12)

    # Thirteen crop c5
    # crop_img_13 = currentImage[625:647, 77:720]
    # imgArray.append(crop_img_13)

    # Fourteen crop c5
    # crop_img_14 = currentImage[625:647, 77:720]
    # imgArray.append(crop_img_14)

    # Fifteen crop C001
    crop_img_15 = currentImage[755:780, 77:310]
    imgArray.append(crop_img_15)

    # Sixteen crop C002
    crop_img_16 = currentImage[790:815, 77:310]
    imgArray.append(crop_img_16)

    # Seventeen crop Date 1
    crop_img_17 = currentImage[750:770, 580:740]
    imgArray.append(crop_img_17)

    # Eighteen crop Date 2
    crop_img_18 = currentImage[785:810, 580:740]
    imgArray.append(crop_img_18)

    # Initialise width and height for final picture
    max_width = 0
    total_height = 0


    ############ Get all information from current form #########################################
    for img in imgArray:
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]

    final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)
    alphabet_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)

    current_y = 0
    # keep track of current image placing in terms of Y coordinate
    for img in imgArray:
        final_image[current_y:img.shape[0] + current_y, :img.shape[1], :] = img
        current_y += img.shape[0]

    cv2.imshow('original_img', final_image)
    cv2.waitKey()


# prepTrainData('C:/Users/A/PycharmProjects/CIMB_demo/formData/Alvin/img16.jpg')
# getScanFormDetails('C:/Users/A/PycharmProjects/CIMB_demo/formData/Dad/img18.jpg')
getScanFormDetails2('C:/Users/A/PycharmProjects/CIMB_demo/formData/Cynthia/img15.jpg')






