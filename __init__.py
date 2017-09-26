from client import *

class PesaBot(object):
    def __init__(self, auth):
        self.client = Client(auth.get('email'), auth.get('password'))

    def call(self, path, method='GET', payload=None):
        return self.client.call(path, method, payload)
    