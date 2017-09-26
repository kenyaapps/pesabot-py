import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://pesabot.com/api/v1/'

class Client(object):
    def __init__(self, email, password):
        self.auth = HTTPBasicAuth(email, password)

    def call(self, path, method='GET', payload={}):
        if method == 'POST':
            res = requests.post(BASE_URL+path, data=payload, auth=self.auth)
        else:
            res = requests.get(BASE_URL+path, auth=self.auth)
        return {'data': res.json(), 'status': res.status_code} 

    