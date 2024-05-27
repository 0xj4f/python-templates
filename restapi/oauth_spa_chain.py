import hashlib
import base64
import os
import urllib.parse
import requests
import json

"""
https://manage.auth0.com/dashboard

Go to Application Details, credentials tab
Make sure Application Authentication is set to None, POST will make you unauthorized
https://stackoverflow.com/questions/63558632/login-with-auth0-was-successful-but-still-a-401-access-denied-is-returned
"""

class OAuth2Client:
    def __init__(self, client_id, redirect_uri, base_url):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.base_url = base_url

    def generate_code_verifier(self, length=45):
        verifier = base64.urlsafe_b64encode(os.urandom(length)).rstrip(b'=').decode('utf-8')
        return verifier

    def generate_code_challenge(self, verifier):
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('utf-8')).digest()).rstrip(b'=').decode('utf-8')
        return challenge

    def create_authorization_request_url(self, state, code_challenge):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'state': state,
            'redirect_uri': self.redirect_uri,
            'code_challenge': code_challenge,
            'code_challenge_method': 'S256'
        }
        return self.base_url + "authorize?" + urllib.parse.urlencode(params)

    def exchange_code_for_token(self, code, code_verifier):
        token_url = self.base_url + "oauth/token"
        data = {
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'code_verifier': code_verifier,
            'code': code
        }
        response = requests.post(token_url, data=data)
        return response.json()

if __name__ == "__main__":
    client_id = "xxxxxxxxxxxxxxxxx" # CHANGE ME
    redirect_uri = "https://example-app.com/redirect"
    base_url = "https://dev-XXXXXXXXXXXX.us.auth0.com/" # CHANGE ME

    oauth_client = OAuth2Client(client_id, redirect_uri, base_url)
    state = base64.urlsafe_b64encode(os.urandom(16)).rstrip(b'=').decode('utf-8')  # Generate a random state
    code_verifier = oauth_client.generate_code_verifier()
    code_challenge = oauth_client.generate_code_challenge(code_verifier)
    authorization_url = oauth_client.create_authorization_request_url(state, code_challenge)

    print(f"Code Verifier: {code_verifier}")
    print(f"Code Challenge: {code_challenge}\n")
    print(f"Open Authorization URL: \n{authorization_url} \n\n")

    new_code = input("Enter the new code from the URL: \n")
    token_response = oauth_client.exchange_code_for_token(new_code, code_verifier)
    print(json.dumps(token_response, indent=2))

"""
Example:
python3 oauth-spa-chain.py
Code Verifier: EES3OOKXVs9aQgwhU07kM-pDlktSJnTWEHT4S9J7oHOwz43x5jJgsY0vOhMw
Code Challenge: wsg-WLx_8h9o1O2UcNMMzmH7xOyRaQcXeE-puMbIF0c

Open Authorization URL:
https://dev-XXXXXXXXXXXX.us.auth0.com/authorize?response_type=code&client_id=jQwtHmqRQxkJGuynKAjm8L6JVKPN4Lfl&state=ZX7E4sFqrH0wfwPy7_A_qg&redirect_uri=https%3A%2F%2Fexample-app.com%2Fredirect&code_challenge=wsg-WLx_8h9o1O2UcNMMzmH7xOyRaQcXeE-puMbIF0c&code_challenge_method=S256


Enter the new code from the URL:
eeGSehX54biUci_qj_vEUcH0IE-1JLQO5GUkpFuXuG_oU
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpXaFJFVFc3MHFGVWNoSElHeFlyeiJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMWwyc3Q3N2praDNleGVhLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODc5MDMwNjA4MzUzOTY4MjM0NyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tIiwiaWF0IjoxNzE2Nzc5Nzg0LCJleHAiOjE3MTY4NjYxODQsImF6cCI6ImpRd3RIbXFSUXhrSkd1eW5LQWptOEw2SlZLUE40TGZsIn0.QZ-fSUE2hnPc1S907aGbSmd2diZT4Qy7SF_Sfh-Jf_0w8NEutjCpYyUxq6G3YN4dd3rAH3GQAXxk5NCxjNtVEQhP0hVVNMP1kPR14c2k5lXVrNfbFf4u8VYzhPafilGT-1Xw-kiGB8m330J57vpOn58ArHvHbJSp7mW7ttjUXN88WufGD169iZ7pnjY88MtiFKZzz0sE4BzJ6-lkF3H-62O7Jk1ZMDz-CHpLPGYq6kvrHtJMHx3AOu6g4Pq6eU60WWTeyFtqwCZA8odQ3YTPmWyzSn_WaRctgHQyFhP8xaAjrHeZg0qGO3bUjNHUPUX_B4t4oDOY4nfhamEiGjBs6A",
  "expires_in": 86400,
  "token_type": "Bearer"
}
"""
