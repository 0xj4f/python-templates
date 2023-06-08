import requests

class RestAPIClientBase: 
    def __init__(self) -> None:
        self.session = requests.Session()
    
    def auth(self, url, request, headers={}):
        pass
    
    def get(self, url, headers={}):
        request = requests.Request('GET', url).prepare()
        self.auth(url, request, headers)
        session = requests.Session()
        return session.send(request)

    def post(self, url, headers={}, payload=None):
        request = requests.Request('POST', url).prepare()
        self.auth(url, request, headers)
        request.prepare_body(data=None, files=None, json=payload)
        session = requests.Session()
        return session.send(request)

    def put(self, url, headers={}, payload=None):
        request = requests.Request('PUT', url).prepare()
        self.auth(url, request, headers)
        request.prepare_body(data=None, files=None, json=payload)
        session = requests.Session()
        return session.send(request)

    def patch(self, url, headers={}, payload=None):
        request = requests.Request('PATCH', url).prepare()
        self.auth(url, request, headers)
        request.prepare_body(data=None, files=None, json=payload)
        session = requests.Session()
        return session.send(request)

    def delete(self, url, headers={}):
        request = requests.Request('DELETE', url).prepare()
        self.auth(url, request, headers)
        session = requests.Session()
        return session.send(request)

class RestAPIClient(RestAPIClientBase):
    # AUTH is always different from every website
    def auth(self, url, request, headers={}):        
        request_headers = headers

        request_headers.update(headers)
        request.prepare_headers(request_headers)

if  __name__ == '__main__':
    data = [ 1, 2 ,3]

    for d in data:
        acid = d.numerator()







