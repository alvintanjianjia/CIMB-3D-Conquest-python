import numpy as np
import cv2
import math
from math import atan2, degrees
import random as rng

rng.seed(12345)

def GetAngleOfLineBetweenTwoPoints(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return degrees(atan2(yDiff, xDiff))

def GetLengthBetweenTwoPoints(p1, p2):
    xDiff = abs(p2[0] - p1[0])
    yDiff = abs(p2[1] - p1[1])
    return math.sqrt(xDiff**2 + yDiff**2)

# print(GetLengthBetweenTwoPoints((0,0), (3,4)))
def getSignaturePrediction(path):
    img = cv2.imread(path)
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, channels = img.shape
    # print(height, width, channels)

    # The minimum line length for processing
    # Calculated by getting diagonal of picture, then 15% of the diagonal
    minLineLength = np.sqrt(height ** 2 + width ** 2) * 5 / 100
    # print(minLineLength, "minlinelength")


    cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    greyscale = cv2.Canny(greyscale, 10, 250)
    minLineLength = 100
    maxLineGap = 1
    # lines = cv2.HoughLinesP(greyscale, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    # for i in range(len(lines)):
    #     for x1, y1, x2, y2 in lines[i]:
    #         i += 1
    # cv2.imshow('Hough Transform', img)
    # cv2.waitKey(0)

    imgContour2, contours, hierarchy = cv2.findContours(greyscale.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(hierarchy, 'hierarchy')
    # computes the bounding box for the contour, and draws it on the frame,
    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    centers = [None] * len(contours)
    radius = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])



    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        # cv2.drawContours(img, contours_poly, i, color)
        cv2.rectangle(img, (int(boundRect[i][0]), int(boundRect[i][1])),
                     (int(boundRect[i][0] + boundRect[i][2]), int(boundRect[i][1] + boundRect[i][3])), color, 2)
        cv2.circle(img, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

    for item in boundRect:
        print(item)

    # cv2.drawContours(img, contours, -1, (0, 0, 255), 5)

    lineArray = []
    for i in range(len(contours)):
        if (len(contours[i])) > 1:
            for j in range(len(contours[i]) - 1):
                current = contours[i][j]


                current = contours[i][j]
                next = contours[i][j + 1]

                currentStartX = current[0][0]
                currentStartY = current[0][1]
                currentEndX = next[0][0]
                currentEndY = next[0][1]

                lineArray.append([(currentStartX, currentStartY), (currentEndX, currentEndY)])

    # for element in lineArray:
        # print(element)

    mainLineArray = []
    horizontalLineArray = []
    verticalLineArray = []
    counter = 0
    newLine = True
    arrayCounter = []
    for i in range(1, len(lineArray)):
        if newLine is True:
            ("run this part")
            original = lineArray[i]
            newLine = False
        current = lineArray[i]
        previous = lineArray[i - 1]
        if abs(current[0][0] - current[1][0] > minLineLength) or abs(current[1][0] - current[1][1]) > minLineLength:
            if abs(original[0][0] - current[1][0]) > minLineLength or abs(
                    original[0][1] - current[1][1]) > minLineLength:

                cv2.line(img, original[0], current[1], (255, 0, 0), 10)
                angle = abs(GetAngleOfLineBetweenTwoPoints(original[0], current[1]))
                # print(angle, "angle")
                if angle <= 46 or angle >= 135:
                    # print("horizontal added")
                    distance = GetLengthBetweenTwoPoints(original[0], current[1])
                    horizontalLineArray.append((distance, [original[0], current[1]]))
                else:
                    # print("vertical added")
                    distance = GetLengthBetweenTwoPoints(original[0], current[1])
                    verticalLineArray.append((distance,[original[0], current[1]]))
                # print([original[0], current[1]], "original + current")
                mainLineArray.append([original[0], current[1]])
                newLine = True

    verticalLineArray.sort()
    horizontalLineArray.sort()
    totalLenVert = 0
    totalLenHor = 0
    maxLenVert = 0
    minLenVert = 10**10
    maxLenHor = 0
    minLenHor = 10**10

    # Get statistics on the signature
    for element in verticalLineArray:
        totalLenVert += element[0]
        if element[0] < minLenVert:
            minLenVert = element[0]
        if element[0] > maxLenVert:
            maxLenVert = element[0]

    # Get statistics on the signature
    for element in horizontalLineArray:
        totalLenHor += element[0]
        if element[0] < minLenHor:
            minLenHor = element[0]
        if element[0] > maxLenHor:
            maxLenHor = element[0]

    if minLenVert == 10**10:
        minLenVert = 0

    if minLenHor == 10**10:
        minLenHor = 0

    if len(verticalLineArray) == 0:
        avgVertLen = 0
    else:
        avgVertLen = totalLenVert / len(verticalLineArray)

    if len(horizontalLineArray) == 0:
        avgHorLen = 0
    else:
        avgHorLen = totalLenHor / len(horizontalLineArray)
    # print(len(mainLineArray), "mainLineArray")
    # print(len(verticalLineArray), "verticalLineArray")
    # print(len(horizontalLineArray), "horizontalLineArray")

    cv2.imshow('lines reproduced', img)
    cv2.waitKey(0);
    return avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert
    # return len(mainLineArray), len(verticalLineArray), len(horizontalLineArray)


avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction("test_background.jpg")
# avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction("formDataTraining/Alvin/img14_0.jpg")
print(avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert)
print("haha fk u")
# getSignaturePrediction('forgeSet/alvin_forge_1/20181128_183513.png')