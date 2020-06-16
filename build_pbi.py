# -*- coding: utf-8 -*-
"""
@author: Tadeu Mansi
"""
import requests
from requests_toolbelt import MultipartEncoder
import json

url = "https://login.microsoftonline.com/common/oauth2/token"

payload = {
'client_id': 'client_id_azure',
'grant_type': 'password',
'resource': 'https://analysis.windows.net/powerbi/api',
'username': 'seuemail',
'password': 'sua senha',
'client_secret': 'seu client secret'
}

response = requests.request("POST", url, headers={}, data = payload)

json_encode = json.loads(response.text.encode('utf8'))
accessToken = json_encode['access_token']

groupId = "id do workspace"
reportName = "f1"

url = 'https://api.powerbi.com/v1.0/myorg/groups/' + groupId + '/imports?datasetDisplayName=' + reportName + '&nameConflict=CreateOrOverwrite'

headers = {
    'Content-Type': 'multipart/form-data',
    'authorization': 'Bearer ' + accessToken
}

file_location = 'nome do seu relatorio.pbix'

files = {'value': (None, open(file_location, 'rb'), 'multipart/form-data')}
mp_encoder = MultipartEncoder(fields=files)

r = requests.post(
    url=url,
    data=mp_encoder, 
    headers=headers
)
