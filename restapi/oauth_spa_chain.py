import hashlib
import base64
import os
import requests
import urllib.parse
import json

"""
https://manage.auth0.com/dashboard

Go to Application Details, credentials tab
Make sure Application Authentication is set to None, POST will make you unauthorized
https://stackoverflow.com/questions/63558632/login-with-auth0-was-successful-but-still-a-401-access-denied-is-returned
"""
def generate_code_verifier(length=45):
    verifier = base64.urlsafe_b64encode(os.urandom(length)).rstrip(b'=').decode('utf-8')
    return verifier

def generate_code_challenge(verifier):
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('utf-8')).digest()).rstrip(b'=').decode('utf-8')
    return challenge

def create_authorization_request_url(client_id, state, redirect_uri, code_challenge):
    base_url = "https://dev-XXXXXXXXXX.us.auth0.com/authorize?" # CHANGE ME
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'state': state,
        'redirect_uri': redirect_uri,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256'
    }
    return base_url + urllib.parse.urlencode(params)

def exchange_code_for_token(code, code_verifier):
    token_url = "https://dev-XXXXXXXXXXX.us.auth0.com/oauth/token" # CHANGE ME
    client_id = "XXXXXXXXXX" # CHANGE ME
    redirect_uri = "https://example-app.com/redirect"

    data = {
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'code_verifier': code_verifier,
        'code': code
    }

    response = requests.post(token_url, data=data)
    return response.json()

if __name__ == "__main__":
    client_id = "CHANGE ME"
    state = base64.urlsafe_b64encode(os.urandom(16)).rstrip(b'=').decode('utf-8')  # Generate a random state
    redirect_uri = "https://example-app.com/redirect"
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)
    authorization_url = create_authorization_request_url(client_id, state, redirect_uri, code_challenge)

    print(f"Code Verifier: {code_verifier}")
    print(f"Code Challenge: {code_challenge}\n")
    print(f"Open Authorization URL: \n{authorization_url} \n\n")

    new_code = input("Enter the new code from the url \n")
    token_response = exchange_code_for_token(new_code, code_verifier)
    print(json.dumps(token_response))
