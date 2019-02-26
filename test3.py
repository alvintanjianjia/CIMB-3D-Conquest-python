from imageProcessing import *
import csv
import glob
import os
from csvCreator import *
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

credentials = service_account.Credentials.from_service_account_file('C:/Users/tanji/Downloads/cimb-demo-222703-87bf0bdd7194.json')

project_id = 'cimb-demo-222703.cimb_demo.cimb_demo_time'

client = bigquery.Client(credentials=credentials,project=project_id)

def test_insert_record2(test):
    schema = [
        bigquery.SchemaField('username', 'STRING', mode='NULLABLE'),
        bigquery.SchemaField('number_of_login', 'INTEGER', mode='NULLABLE'),
        bigquery.SchemaField('min_login_time', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('max_login_time', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('avg_login_time', 'FLOAT', mode='NULLABLE'),
    ]
    query_job = client.insert_rows('cimb-demo-222703.cimb_demo.cimb_demo_time', test, schema)

test =  [('Alvin', 1, 2000, 4500, 3150)]
test_insert_record2(test)