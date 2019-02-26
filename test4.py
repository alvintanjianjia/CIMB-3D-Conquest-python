import base64
import time
import math


def encode(key, string):
    enc = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(string[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

millis = int(round(time.time() * 1000))
print(millis)
millis = math.ceil(millis/100000000)
print(millis)

key = "haha"
string = 'This is funny'

enc = encode(key,string)
print(enc)
print(decode(key,enc))

#Read the image
# img = cv2.imread('dataTrainingSet/Alvin/20181116_023403.png')
# img = cv2.imread('forgeSet/alvin_forge_1/20181128_183513.png')
# img = cv2.imread('alvin_test_signature.png')
# greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height, width, channels = img.shape
# print(height, width, channels)

# The minimum line length for processing
# Calculated by getting diagonal of picture, then 15% of the diagonal
# minLineLength = np.sqrt(height**2 + width**2) * 5 / 100
# print(minLineLength, "minlinelength")
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# greyscale = cv2.Canny(greyscale, 10, 250)
# minLineLength = 100
# maxLineGap = 1
# lines = cv2.HoughLinesP(greyscale, 1, np.pi/180, 100, minLineLength, maxLineGap)
# for i in range(len(lines)):
#     for x1,y1,x2,y2 in lines[i]:
#         i += 1
#
        # print((x1, y1), "Point 1")
        # print((x2, y2), 'Point 2')
        # cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)
# cv2.imshow('Hough Transform', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# imgContour2, contours, hierarchy = cv2.findContours(greyscale.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#contours = sorted(contours, key=cv2.contourArea, reverse=True)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:25]


# cv2.imshow('contours', greyscale)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(len(contours))
# print(contours)
# lineArray = []
# for i in range(len(contours)):
#     if (len(contours[i])) > 1:
#         for j in range(len(contours[i]) - 1):
#             current = contours[i][j]
#             print(current, "current here")
            # if j == len(contours[i] - 1) and len(current[0]) > 1:
                # break

            # current = contours[i][j]
            # next = contours[i][j+1]
            # print(current[0][0])
            # currentStartX = current[0][0]
            # currentStartY = current[0][1]
            # currentEndX = next[0][0]
            # currentEndY = next[0][1]
            # print(currentStartX, currentEndX, "current start and end X coordinates")
            # print(currentStartY, currentEndY, "current start and end Y coordinates")
            # cv2.line(img, (currentStartX, currentStartY), (currentEndX, currentEndY), (255, 0, 0), 1)
            # lineArray.append([(currentStartX, currentStartY), (currentEndX, currentEndY)])
            # cv2.line(img, contours[i][j], contours[i][j], (255, 0, 0), 100)

# for element in lineArray:
#     print(element)

# mainLineArray = []
# horizontalLineArray = []
# verticalLineArray = []
# counter = 0
# newLine = True
# arrayCounter = []
# for i in range(1,len(lineArray)):
#     if newLine is True:
#         ("run this part")
#         original = lineArray[i]
#         newLine = False
#     current = lineArray[i]
#     previous = lineArray[i-1]
#     if abs(current[0][0] - current[1][0] > minLineLength) or abs(current[1][0] - current[1][1]) > minLineLength:
#         if abs(original[0][0] - current[1][0]) > minLineLength or abs(original[0][1] - current[1][1]) > minLineLength:
#
#             cv2.line(img, original[0], current[1], (255, 0, 0), 10)
#             angle = abs(GetAngleOfLineBetweenTwoPoints(original[0], current[1]))
#             print(angle, "angle")
#             if angle <= 46 or angle >= 135:
#                 print("horizontal added")
#                 horizontalLineArray.append([original[0], current[1]])
#             else:
#                 print("vertical added")
#                 verticalLineArray.append([original[0], current[1]])
#             print([original[0], current[1]], "original + current")
#             mainLineArray.append([original[0], current[1]])
#             newLine = True
#
# print(len(mainLineArray), "mainLineArray")
# print(len(verticalLineArray), "verticalLineArray")
# print(len(horizontalLineArray), "horizontalLineArray")
#

# for i in range(len(lineArray)):
#     if i == 0:
#         firstStartX = lineArray[0][0][0]
#         firstEndX = lineArray[0][1][0]
#         previousStartX = lineArray[0][0][0]
#         previousEndX = lineArray[0][1][0]
#         previousStartY = lineArray[0][0][1]
#         previousEndY = lineArray[0][1][1]
#
#     elif newLine is True:
#         counter = i
#         print(counter, "counter")
        # firstStartX = lineArray[counter-1][0][0]
        # firstStartY = lineArray[counter-1][0][1]
        # print(firstStartX, firstStartY, "firstStartX and firstStartY")
        # currentStartX = lineArray[i][0][0]
        # currentStartY = lineArray[i][0][1]
        # currentEndX = lineArray[i][1][0]
        # currentEndY = lineArray[i][1][1]
        # previousStartX = lineArray[i-1][0][0]
        # previousEndX = lineArray[i-1][1][0]
        # previousStartY = lineArray[i-1][0][1]
        # previousEndY = lineArray[i-1][1][1]
        # newLine = False
    # else:
    #     currentStartX = lineArray[i][0][0]
    #     currentStartY = lineArray[i][0][1]
    #     currentEndX = lineArray[i][1][0]
    #     currentEndY = lineArray[i][1][1]
    #     previousStartX = lineArray[i-1][0][0]
    #     previousStartY = lineArray[i-1][0][1]
        # previousEndX = lineArray[i-1][1][0]
        # previousEndY = lineArray[i-1][1][1]
        # if abs(currentStartX - previousEndX) > minLineLength or abs(currentStartY - previousEndY) > minLineLength:
        #     mainLineArray.append([(firstStartX, firstStartY), (previousEndX, previousEndY)])
        #     mainLineArray.append([(firstStartX, firstStartY), (currentEndX, currentEndY)])
            # print(firstStartX, firstStartY, previousEndX, previousEndY, "start and previous coordinates")
            # cv2.line(img, (firstStartX, firstStartY), (currentEndX, firstStartY), (255, 0, 0), 10)
            # cv2.line(img, (firstStartX, firstStartY), (firstStartX, currentEndY), (255, 0, 0), 10)
            #
            # newLine = True


        # previousStartX = currentStartX
        # previousStartY = currentStartY
        # previousEndX = currentEndX
        # previousEndY = currentEndY

# print(len(mainLineArray), "length of mainLineArray")
# for element in mainLineArray:
    # print(element)
# print("finished printing mainLineArray")
    # print(element)
# print("line Drawn")
# cv2.imshow('lines reproduced', img)
# cv2.waitKey(0);
# cv2.destroyAllWindows()



# imgTest = imgContour2.copy()
# cv2.drawContours(imgTest, contours, 1, (0, 255, 0), 3)
# cv2.imshow('image', imgTest)
# cv2.waitKey(0)
# cv2.destroyAllWindows()