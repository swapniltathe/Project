from re import template
from urllib import response
import requests
import json
import base64
import sys

username = "admin"
password = "Ansible123!"
templateid = sys.argv[1]
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

url = 'http://192.168.1.12:30080/api/v2/job_templates/'+templateid+'/launch/'

headers = {
    'Authorization': "Basic " + base64string,
    'Content-Type': 'application/json'
}

data = {
    "extra_vars": {
        "naav": "Jalebi bai",
        "gaav": "Wasseypur"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)