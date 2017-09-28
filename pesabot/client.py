import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://pesabot.com/api/v1/'

class Client(object):
    def __init__(self, email, password):
        self.auth = None
        if email and password:
            self.auth = HTTPBasicAuth(email, password)

    def call(self, path, method, payload={}):
        if method == 'POST':
            res = requests.post(BASE_URL+path, json=payload, auth=self.auth)
        elif method == 'PUT':
            res = requests.put(BASE_URL+path, json=payload, auth=self.auth)
        elif method == 'DELETE':
            res = requests.delete(BASE_URL+path, auth=self.auth)
        else:
            res = requests.get(BASE_URL+path, auth=self.auth)
        return {'data': res.json(), 'status': res.status_code} 

    
