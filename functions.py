import numpy as np
import cv2
import csv
import math
from math import atan2, degrees
import tensorflow as tf
import csv
import glob
import io

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    result_array = []
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))
                    result_array.append((word_text, word.confidence))
                    # for symbol in word.symbols:
                    #     print('\tSymbol: {} (confidence: {})'.format(
                    #         symbol.text, symbol.confidence))
    return result_array

def prepTrainData(path, name=None):
    currentImage = cv2.imread(path)

    scale_percent = 50  # percent of original size
    width = int(currentImage.shape[1] * scale_percent / 100)
    height = int(currentImage.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    currentImage = cv2.resize(currentImage, dim, interpolation=cv2.INTER_AREA)
    print('Original Dimensions : ', currentImage.shape)
    baseString = 'C:/Users/A/PycharmProjects/CIMB_demo/' + name
    # y first then x
    imgArray = []

    # First crop Student_ID number
    crop_img_1 = currentImage[260:290, 395:690]
    imgArray.append(crop_img_1)

    cv2.imwrite('C:/Users/A/PycharmProjects/CIMB_demo/')

    # Second crop Last_Name
    crop_img_2 = currentImage[285:320, 150:365]
    imgArray.append(crop_img_2)

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

    # cv2.imshow('original_img', final_image)
    # cv2.waitKey()


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


    current_y = 0
    # keep track of current image placing in terms of Y coordinate
    for img in imgArray:
        final_image[current_y:img.shape[0] + current_y, :img.shape[1], :] = img
        current_y += img.shape[0]

    # cv2.imshow('original_img', final_image)


    # username = filename[-2]
    # filename = filename[-1]
    # baseString = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataTraining/' + username + '/' + filename
    # cv2.imwrite(filename, crop_img_2)
    # cv2.waitKey()


def prepTrainForm2(pathname):


    currentImage = cv2.imread(pathname)
    filename = pathname.replace('\\', '/')
    filename = filename.split("/")
    username = filename[-2]
    filename = filename[-1]
    baseString = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataTraining/' + username + '/'
    counter = 0
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + username + '/' + filename + '_' + str(counter)




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
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'

    cv2.imwrite(currentString, crop_img_1)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1
    annotations = '28269837'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Second crop Last_Name
    crop_img_2 = currentImage[275:310, 150:365]
    imgArray.append(crop_img_2)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_2)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'ALVIN JIAN JIA'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Third crop First_Name
    crop_img_3 = currentImage[281:310, 470:700]
    imgArray.append(crop_img_3)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_3)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'TAN'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fourth crop Course_Name
    crop_img_4 = currentImage[317:345, 170:700]
    imgArray.append(crop_img_4)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_4)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'SOFTWARE ENGINEERING'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fifth crop unit code
    crop_img_5 = currentImage[390:420, 135:250]
    imgArray.append(crop_img_5)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_5)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'FIT3145'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Sixth crop semester
    # crop_img_6 = currentImage[405:425, 370:400]
    # imgArray.append(crop_img_6)

    # Seventh crop year
    crop_img_7 = currentImage[390:415, 605:730]
    imgArray.append(crop_img_7)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_7)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = '2018'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Eighth crop unit title
    crop_img_8 = currentImage[420:445, 130:720]
    imgArray.append(crop_img_8)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_8)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'ADVANCE ALGORITHM AND DATA STRUCTURE'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Ninth crop c1
    crop_img_9 = currentImage[520:540, 77:750]
    imgArray.append(crop_img_9)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_9)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'Student is able to handle advanced data structures and'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

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
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_15)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'IAN LIM WERN HAN'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Sixteen crop C002
    crop_img_16 = currentImage[790:815, 77:310]
    imgArray.append(crop_img_16)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_16)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'IAN LIM WERN HAN'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Seventeen crop Date 1
    crop_img_17 = currentImage[750:770, 580:740]
    imgArray.append(crop_img_17)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_17)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = '27/11/2018'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Eighteen crop Date 2
    crop_img_18 = currentImage[785:810, 580:740]
    imgArray.append(crop_img_18)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_18)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = '27/11/2018'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass


    # Initialise width and height for final picture
    max_width = 0
    total_height = 0


    ############ Get all information from current form #########################################
    for img in imgArray:
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]

    final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)


    current_y = 0
    # keep track of current image placing in terms of Y coordinate
    for img in imgArray:
        final_image[current_y:img.shape[0] + current_y, :img.shape[1], :] = img
        current_y += img.shape[0]

    # cv2.imshow('original_img', final_image)


    baseString2 = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataExtraction/' + username + '/' + filename
    cv2.imwrite(baseString2, final_image)
    result_array = detect_document(baseString2)
    # cv2.waitKey()

    return result_array


def prepTrainForm(pathname):

    currentImage = cv2.imread(pathname)
    print(pathname, "here 2")
    filename = pathname.split('\\')
    username = filename[-2]
    filename = filename[-1]
    counter = 0
    baseString = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataTraining/'+ username + '/'



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

    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    print(currentString)
    cv2.imwrite(currentString, crop_img_1)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = '28269837'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass


    # Second crop Last_Name
    crop_img_2 = currentImage[285:320, 150:365]
    imgArray.append(crop_img_2)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_2)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'ALVIN JIAN JIA'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Third crop First_Name
    crop_img_3 = currentImage[291:320, 470:700]
    imgArray.append(crop_img_3)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_3)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'TAN'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fourth crop Course_Name
    crop_img_4 = currentImage[327:350, 170:700]
    imgArray.append(crop_img_4)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_4)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'SOFTWARE ENGINEERING'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fifth crop unit code
    crop_img_5 = currentImage[407:430, 135:250]
    imgArray.append(crop_img_5)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_5)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1
    annotations = 'FIT3145'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Sixth crop semester
    # crop_img_6 = currentImage[405:425, 370:400]
    # imgArray.append(crop_img_6)

    # Seventh crop year
    crop_img_7 = currentImage[400:425, 605:730]
    imgArray.append(crop_img_7)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_7)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = '2018'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Eighth crop unit title
    crop_img_8 = currentImage[430:455, 130:720]
    imgArray.append(crop_img_8)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_8)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'ADVANCE ALGORITHM AND DATA STRUCTURE'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Ninth crop c1
    crop_img_9 = currentImage[530:550, 77:720]
    imgArray.append(crop_img_9)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_9)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'Student is able to cope'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Tenth crop c2
    crop_img_10 = currentImage[555:575, 77:720]
    imgArray.append(crop_img_10)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_10)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = 'Student took a previous similar unit'
    # for i in range(len(result_array)):
    #     annotations += result_array[i][0] + ','
    # annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Eleventh crop c3
    crop_img_11 = currentImage[580:600, 78:720]
    imgArray.append(crop_img_11)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_11)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Twelve crop c4
    crop_img_12 = currentImage[603:624, 77:720]
    imgArray.append(crop_img_12)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_12)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Thirteen crop c5
    crop_img_13 = currentImage[625:647, 77:720]
    imgArray.append(crop_img_13)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_13)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fourteen crop c5
    crop_img_14 = currentImage[625:647, 77:720]
    imgArray.append(crop_img_14)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_14)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Fifteen crop C001
    crop_img_15 = currentImage[765:790, 77:310]
    imgArray.append(crop_img_15)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    print(currentString)
    cv2.imwrite(currentString, crop_img_15)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Sixteen crop C002
    crop_img_16 = currentImage[800:825, 77:310]
    imgArray.append(crop_img_16)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_16)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Seventeen crop Date 1
    crop_img_17 = currentImage[760:780, 580:740]
    imgArray.append(crop_img_17)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_17)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Eighteen crop Date 2
    crop_img_18 = currentImage[795:820, 580:740]
    imgArray.append(crop_img_18)
    currentString = baseString + filename.split('.')[0] + '_' + str(counter) + '.jpg'
    cv2.imwrite(currentString, crop_img_18)
    result_array = detect_document(currentString)
    fullPath = 'gs://cimb-demo-222703-vcm/formData/formDataTraining' + '/' + username + '/' + filename.split('.')[0] + '_' + str(
        counter) + '.jpg'
    counter += 1

    annotations = ''
    for i in range(len(result_array)):
        annotations += result_array[i][0] + ','
    annotations = annotations[:-1]
    try:
        with open('form_training.csv', mode='a', newline='') as signature_file:
            signature_writer = csv.writer(signature_file)
            signature_writer.writerow([fullPath, annotations])
    except:
        pass

    # Initialise width and height for final picture
    max_width = 0
    total_height = 0


    ############ Get all information from current form #########################################
    for img in imgArray:
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]

    final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)


    current_y = 0
    # keep track of current image placing in terms of Y coordinate
    for img in imgArray:
        final_image[current_y:img.shape[0] + current_y, :img.shape[1], :] = img
        current_y += img.shape[0]

    # cv2.imshow('original_img', final_image)



    baseString2 = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataExtraction/' + username + '/' + filename
    cv2.imwrite(baseString2, final_image)
    result_array = detect_document(baseString2)
    return result_array


    # cv2.waitKey()