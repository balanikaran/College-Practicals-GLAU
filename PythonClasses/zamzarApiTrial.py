import requests
from requests.auth import HTTPBasicAuth

api_key = '6157d028ac3c7e1eeb82c1e71686c4349dcb1a37'
endpoint = "https://sandbox.zamzar.com/v1/jobs"
source_file = "/tmp/portrait.gif"
target_format = "png"

file_content = {'source_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
print (res.json())