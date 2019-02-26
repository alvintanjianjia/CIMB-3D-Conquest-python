import io
import os
from google.cloud import automl_v1beta1
from google.oauth2 import service_account
import time
import json
from functions import *
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
credentials = service_account.Credentials.from_service_account_file('C:/Users/A/Downloads/cimb-demo-222703-87bf0bdd7194.json')



project_id = 'cimb-demo-222703.cimb_demo.cimb_demo_time'
client = vision.ImageAnnotatorClient(credentials=credentials)

# The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'test_word.jpg')

t0 = time.time()

file_name = 'C:/Users/A/PycharmProjects/CIMB_demo/formDataExtraction/Alvin/img14.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
# response = client.text_detection(image=image)
# print(response)
result_array = detect_document(file_name)
print('view result array')
for item in result_array:
    print(item)
# response_json = json.loads(response)
# print(response_json)
# print(response)
# labels = response.label_annotations



t1 = time.time()
print(t1 - t0, 'time')