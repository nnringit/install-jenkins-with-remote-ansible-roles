# Script to check a Jenkins job is SUCCESS or FAILED

import requests, pprint

resp=requests.get(url='http://localhost:8080/job/test/api/json?pretty=true')
if resp.status_code == 200:
    status= resp.json()['color']
    if status == 'red':
        print('FAILED')
    else:
        print('SUCCESS')
