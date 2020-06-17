# -*- coding: utf-8 -*-
"""
@author: Tadeu Mansi
"""
import requests
from requests_toolbelt import MultipartEncoder

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
access_token = response.json()["access_token"]
group_id = "id do workspace"
report_name = "f1"

url = 'https://api.powerbi.com/v1.0/myorg/groups/' + group_id + '/imports?datasetDisplayName=' + report_name + '&nameConflict=CreateOrOverwrite'

headers = {
    'Content-Type': 'multipart/form-data',
    'authorization': 'Bearer ' + access_token
}

file_location = 'nome do seu relatorio.pbix'
files = {'value': (None, open(file_location, 'rb'), 'multipart/form-data')}
mp_encoder = MultipartEncoder(fields=files)

r = requests.post(
    url=url,
    data=mp_encoder, 
    headers=headers
)
