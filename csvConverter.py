import csv
import glob
import os

#Get current working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#Get all file names under current folder
outer_file = glob.glob(dir_path+ '\dataTrainingSet\*')
#for file in outer_file:

    #raw_filenames = glob.glob(file + '\*')
    #print(glob.glob(file))





with open('signature.csv', mode='w', newline='') as signature_file:
    signature_writer = csv.writer(signature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for file in outer_file:
        raw_filenames = glob.glob(file + '\*')

        # Reorganise filenames to GCP syntax
        for item in raw_filenames:
            item = item.split("\\")

            label = item[-2]
            fullPath = 'gs://cimb-demo-222703-vcm/' + item[-2] + '/' + item[-1]
            signature_writer.writerow([fullPath, label])
            print(label, fullPath)





print("CSV finish")