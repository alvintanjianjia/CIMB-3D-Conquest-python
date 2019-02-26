from flask import Flask, request, render_template, jsonify
from json import dumps
from google.cloud import automl_v1beta1
from google.oauth2 import service_account
from google.cloud import bigquery
from google.cloud.automl_v1beta1.proto import service_pb2
import sys
import time
import base64
import pandas as pd
from imageProcessing import *
import urllib.request as urllib
# If you are using Python 3+, import urllib instead of urllib2
import json
import requests

credentials = service_account.Credentials.from_service_account_file('C:/Users/A/Downloads/cimb-demo-222703-87bf0bdd7194.json')

project_id = 'cimb-demo-222703.cimb_demo.cimb_demo_time'

client = bigquery.Client(credentials=credentials,project=project_id)



def insert_record_raw(test):
    schema = [
        bigquery.SchemaField('username', 'STRING', mode='NULLABLE'),
        bigquery.SchemaField('login_time', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('avgHor', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('avgVert', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('minHor', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('maxHor', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('minVert', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('maxVert', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('forgeOrReal', 'INTEGER', mode='NULLABLE'),

    ]
    query_job = client.insert_rows('cimb-demo-222703.cimb_demo.raw_dataset_app', test, schema)

def test_insert_record(test):
    schema = [
        bigquery.SchemaField('username', 'STRING', mode='NULLABLE'),
        bigquery.SchemaField('number_of_login', 'INTEGER', mode='NULLABLE'),
        bigquery.SchemaField('avg_login_time', 'FLOAT', mode='NULLABLE')

    ]
    query_job = client.insert_rows('cimb-demo-222703.cimb_demo.cimb_demo_time', test, schema)


def get_time_record(username):
    # username = "alvintest1"
    query_string = "SELECT * FROM cimb_demo.cimb_demo_time WHERE username = '" + username + "'"
    query_job = client.query(query_string, project = 'cimb-demo-222703')
    results = query_job.result()
    results_df = results.to_dataframe()
    usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time = results_df.iloc[0][0], results_df.iloc[0][1], results_df.iloc[0][2], results_df.iloc[0][3], results_df.iloc[0][4]
    # print(usernameTBC, number_of_login, avg_login_time)
    return(usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time)


def get_xy_record(username):
    print(username, 'username at getxyrecord')
    query_string = "SELECT * FROM cimb_demo.username_HorVert WHERE username = '" + username + "'"
    query_job = client.query(query_string, project='cimb-demo-222703')
    results = query_job.result()
    results_df = results.to_dataframe()
    username, dbAvgHor, dbAvgVert, dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert = results_df.iloc[0][0], results_df.iloc[0][1], results_df.iloc[0][2], results_df.iloc[0][3], results_df.iloc[0][4], results_df.iloc[0][5], results_df.iloc[0][6],
    print(username, dbAvgHor, dbAvgVert, dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert)
    return(username, dbAvgHor, dbAvgVert, dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert)


def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned

def create_prediction_image(imageBase64):
    img_data = str.encode(imageBase64)
    with open('imageToPredict.png', 'wb') as fh:
        fh.write(base64.decodebytes(img_data))


app = Flask(__name__)


@app.route("/", methods = ['POST', 'GET'])
def testServerRest():
    paranoidStatement = "server up and running - lol Alvin is paranoid"
    print(paranoidStatement)
    return(paranoidStatement)


@app.route("/xyCheck", methods = ['POST', 'GET'])
def xyCheck(username):
    avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction("imageToPredict.png")
    # requestJSON = request.get_json()
    # username = requestJSON['username']
    usernameDB, dbAvgHor, dbAvgVert, dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert = get_xy_record(username)
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["AvgHorLen", "AvgVertLen", "minLenHor", "maxLenHor", "maxLenVert", "minLenVert",
                                    "ForgeOrReal", "dbAvgHor", "dbAvgVert", "dbAvgMinHor", "dbAvgMaxHor",
                                    "dbAvgMinVert", "dbAvgMaxVert"],
                    "Values": [[avgHorLen, avgVertLen, minLenHor, maxLenHor,
                                maxLenVert, minLenVert, "", dbAvgHor, dbAvgVert,
                                dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert]]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/94a533e5496b40479d6e69075afa124e/services/c8c247d2269b4476a4e4c282a73b9ba3/execute?api-version=2.0&details=true'
    api_key = '5fR3tgStX+Qt1EklwEZV2MWTISen+CTzWrapBzMr+xv4V5Cm8fe3VfPQ5GCc8n8eFQWZRWNY5pZKjMLM8VHwBg=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.Request(url, body, headers)

    try:
        response = urllib.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        encoding = response.info().get_content_charset('utf-8')
        JSON_object = json.loads(result.decode(encoding))
        value = JSON_object['Results']
        value = value['output1']

        value = value['value']

        value = value['Values']
        result = value[0][13]
        result = int(result)
        print(value[0][13])
        # print("fk u why u no come out")
        print(result)
        if result == 0:
            print("its a fake, failed XY test(FOR TESTING PURPOSES)")
        else:
            print("its a genuine, passed XY test (FOR TESTING PURPORSES)")
    except:
        print("The request failed with status code: ")

    return_packet = {
        'result': result
    }
    # response = jsonify(score, answer)
    return result


def xyCheckInner(username):
    avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert = getSignaturePrediction("imageToPredict.png")
    # requestJSON = request.get_json()
    # username = requestJSON['username']
    usernameDB, dbAvgHor, dbAvgVert, dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert = get_xy_record(username)
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["AvgHorLen", "AvgVertLen", "minLenHor", "maxLenHor", "maxLenVert", "minLenVert",
                                    "ForgeOrReal", "dbAvgHor", "dbAvgVert", "dbAvgMinHor", "dbAvgMaxHor",
                                    "dbAvgMinVert", "dbAvgMaxVert"],
                    "Values": [[avgHorLen, avgVertLen, minLenHor, maxLenHor,
                                maxLenVert, minLenVert, "", dbAvgHor, dbAvgVert,
                                dbAvgMinHor, dbAvgMaxHor, dbAvgMinVert, dbAvgMaxVert]]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/94a533e5496b40479d6e69075afa124e/services/c8c247d2269b4476a4e4c282a73b9ba3/execute?api-version=2.0&details=true'
    api_key = '5fR3tgStX+Qt1EklwEZV2MWTISen+CTzWrapBzMr+xv4V5Cm8fe3VfPQ5GCc8n8eFQWZRWNY5pZKjMLM8VHwBg=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.Request(url, body, headers)

    try:
        response = urllib.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        encoding = response.info().get_content_charset('utf-8')
        JSON_object = json.loads(result.decode(encoding))
        value = JSON_object['Results']
        value = value['output1']

        value = value['value']

        value = value['Values']
        result = value[0][13]
        result = int(result)
        print(value[0][13])
        print("fk u why u no come out")
        print(result)
        if result == 0:
            print("its a fake (FOR TESTING PURPOSES)")
        else:
            print("its a genuine (FOR TESTING PURPORSES)")
    except:
        print("The request failed with status code: ")

    return_packet = {
        'result': result
    }
    # response = jsonify(score, answer)
    return result, avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert


def timeCheckInner(username):
    # requestJSON = request.get_json()
    # username = requestJSON['username']
    usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time = get_time_record(username)
    # return_packet = {
    #     "result": "false"
    # }
    # return jsonify(return_packet);
    return (usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time)

@app.route("/timeCheck", methods = ['POST', 'GET'])
def timeCheck(username):
    # requestJSON = request.get_json()
    # username = requestJSON['username']
    usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time = get_time_record(username)
    # return_packet = {
    #     "result": "false"
    # }
    # return jsonify(return_packet);
    return usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time

@app.route("/predictSignatureImage", methods = ['POST', 'GET'])
def predictSignatureImage():
    requestJSON = request.get_json()
    imageBase64 = requestJSON['payload']
    time = requestJSON['time']
    time = float(time)

    imageBase64 = imageBase64['image']
    imageBase64 = imageBase64['imageBytes']

    # print(imageBase64)

    # print(requestJSON['payload'])

    create_prediction_image(imageBase64)

    file_path = 'imageToPredict.png'
    project_id = 'cimb-demo-222703'
    model_id = 'ICN3114570555399011330'

    with open(file_path, 'rb') as ff:
        content = ff.read()


    prediction = get_prediction(content, project_id, model_id)
    score = str(prediction.payload[0].classification.score)
    answer = str(prediction.payload[0].display_name)
    print(score, answer, "score + answer")
    usernameTBC, number_of_login, min_login_time, max_login_time, avg_login_time = timeCheckInner(answer)
    print(time, "user_time")
    print(avg_login_time, 'db_time')
    xyAnswer, avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert= xyCheckInner(answer)
    if (xyAnswer == 1 and float(score) > 0.98 and time > int(min_login_time) and time < int(max_login_time) ):
        forgeReal = 1
        print("REAL, you are " + usernameTBC)
        return_packet = {
            'score' : 1,
            'answer': answer
        }
    else:
        forgeReal = 0
        print("FORGE, stop trying to be " + usernameTBC)
        return_packet = {
            'score' : 0,
            'answer' : answer
        }

    # response = jsonify(score, answer)
    test = [(answer, time, avgHorLen, avgVertLen, minLenHor, maxLenHor, maxLenVert, minLenVert, forgeReal )]
    insert_record_raw(test)
    return jsonify(return_packet)

# Run server
app.run(host = '192.168.0.135')



# if __name__ == '__main__':
#   file_path = sys.argv[1]
#   project_id = sys.argv[2]
#   model_id = sys.argv[3]
#
#   with open(file_path, 'rb') as ff:
#     content = ff.read()
#
#   print(get_prediction(content, project_id,  model_id))


# username = 'alvintest1'
# get_record(username)

#testInsert1 = [('alvintest1', 1, 0.02)]
#test_insert_record(testInsert1)