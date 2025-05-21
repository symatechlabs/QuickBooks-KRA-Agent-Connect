import base64
import urllib.parse

import requests
from Config import CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_CODE, REDIRECT_URI, OAUTH_URL, CONTENT_TYPE_FORM_URL_ENCODED

class QuickBooksConnect:

    def getAuthCode(self):
        params = {
            "client_id" : CLIENT_ID,
            "redirect_uri" : REDIRECT_URI,
            "response_type" : "code",
            "scope" : "com.intuit.quickbooks.accounting",
            "state" : "15874"
        }
        return "https://appcenter.intuit.com/connect/oauth2?" + urllib.parse.urlencode(params)


    def getTokens(self):
        token_url = OAUTH_URL+"/oauth2/v1/tokens/bearer"
        auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": CONTENT_TYPE_FORM_URL_ENCODED
        }

        data = {
            "grant_type": "authorization_code",
            "code": AUTHORIZATION_CODE,
            "redirect_uri": REDIRECT_URI
        }

        response = requests.post(token_url, headers=headers, data=data)
        return response.json()


    def refreshToken(self, refreshToken):
        token_url = OAUTH_URL+"/oauth2/v1/tokens/bearer"
        auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": CONTENT_TYPE_FORM_URL_ENCODED
        }

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refreshToken
        }

        response = requests.post(token_url, headers=headers, data=data)
        return response.json()