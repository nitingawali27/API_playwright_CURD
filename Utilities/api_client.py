import json
from Utilities.headers import APIHeaders

class APIClient:
    def __init__(self, request):
        self.request = request

    def get(self, url):
        response = self.request.get(url)
        print(json.dumps(response.json(), indent=4))
        return response

    def post(self, url, payload: dict):
        response = self.request.post(url, data=json.dumps(payload))
        print(json.dumps(response.json(), indent=4))
        return response

    def put(self, url, payload: dict):
        response = self.request.put(url, data=json.dumps(payload))
        print(json.dumps(response.json(), indent=4))
        return response

    def delete(self, url):
        response = self.request.delete(url)
        return response
