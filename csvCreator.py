import csv


def writeCSV(array, filename, header):
    with open(filename, mode='w', newline='') as signature_file:
        signature_writer = csv.writer(signature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        signature_writer.writerow(header)
        for element in array:
            signature_writer.writerow(element)

