from imageProcessing import *
import csv
import glob
import os
from csvCreator import *

# If genuine == 1, if forge == 0
marker = 1
dict = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
# img = cv2.imread('forgeSet/alvin_forge_1/20181128_183513.png')
# outer_file = glob.glob(dir_path + '\\testSet\*')
outer_file = glob.glob(dir_path + '\dataTrainingSet\*')

print(outer_file)
dataArrayTemp = []
dataArray = []

# Code for genuine signatures
for file in outer_file:
    raw_filenames = glob.glob(file + '\*')
    for item in raw_filenames:
        item = item.split("\\")

        label = item[-2]
    trainingAvgHor = 0
    trainingAvgVert = 0
    trainingAvgMaxHor = 0
    trainingAvgMinHor = 0
    trainingAvgMaxVert = 0
    trainingAvgMinVert = 0
    for element in raw_filenames:
        print(element)
        avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction(element)
        trainingAvgHor += avgHorLen
        trainingAvgVert += avgVertLen
        trainingAvgMaxHor += maxLenHor
        trainingAvgMinHor += minLenHor
        trainingAvgMaxVert += maxLenVert


        trainingAvgMinVert += minLenVert
        dataArrayTemp.append((avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert,1))
    trainingAvgHor = trainingAvgHor/len(dataArrayTemp)
    trainingAvgVert = trainingAvgVert/len(dataArrayTemp)
    trainingAvgMinHor = trainingAvgMinHor/len(dataArrayTemp)
    trainingAvgMaxHor = trainingAvgMaxHor/len(dataArrayTemp)
    trainingAvgMaxVert = trainingAvgMaxVert/len(dataArrayTemp)
    trainingAvgMinVert = trainingAvgMinVert/len(dataArrayTemp)
    for element in dataArrayTemp:
        dataArray.append((element[0], element[1], element[2], element[3], element[4], element[5], element[6], trainingAvgHor, trainingAvgVert, trainingAvgMinHor, trainingAvgMaxHor, trainingAvgMinVert, trainingAvgMaxVert))
    dict[label] = (trainingAvgHor, trainingAvgVert, trainingAvgMinHor, trainingAvgMaxHor, trainingAvgMinVert, trainingAvgMaxVert)




# Code to for forge signatures
outer_file = glob.glob(dir_path + '\\forgeSet\*')
for file in outer_file:
    raw_filenames = glob.glob(file + '\*')
    for item in raw_filenames:
        item = item.split("\\")

        label = item[-2]
    for element in raw_filenames:
        print(element)
        avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction(element)
        db_value = dict.get(label)
        print(db_value, 'dbvalue')
        print(db_value[0])
        dataArray.append((avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert,0, db_value[0], db_value[1], db_value[2], db_value[3], db_value[4], db_value[5]))

writeCSV(dataArray, 'mlTraining.csv', ["AvgHorLen", "AvgVertLen", "minLenHor", "maxLenHor", "maxLenVert", "minLenVert", "ForgeOrReal","dbAvgHor", "dbAvgVert", "dbAvgMinHor", "dbAvgMaxHor", "dbAvgMinVert", "dbAvgMaxVert"])
# getSignaturePre
# diction()

