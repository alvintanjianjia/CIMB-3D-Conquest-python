from functions import *
import os
import csv
import glob

#Get current working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)



#Get all file names under current folder
outer_file = glob.glob(dir_path+ '\\formData\\*')
# print(outer_file)

for file in outer_file:
    # for item in file:
        # print(item)

    trainingDir = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataTraining/'
    extractionDir = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataExtraction/'
    os.makedirs(trainingDir + file.split('\\')[-1])
    os.makedirs(extractionDir + file.split('\\')[-1])
    raw_filenames = glob.glob(file + '\*')



    # for innner1 in raw_filenames:
        # img2process = glob.glob(file + '\*')
        # print(glob.glob)

    for item in raw_filenames:
        path = item


        item = item.split('\\')

        print(item[-2], item[-1], path)

        if item[-2] == "Cynthia" or item[-2] == 'Chailam':

            result_array = prepTrainForm2(path)



        else:


            result_array = prepTrainForm(path)






# prepTrainData('C:/Users/A/PycharmProjects/CIMB_demo/formData/Alvin/img16.jpg')