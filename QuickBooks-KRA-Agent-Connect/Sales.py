import requests

from Config import CONTENT_TYPE_TEXT, SANDBOX_URL
class Sales:

    def getSalesReceipts(self, accessToken, companyID, maxResults):
        url = f"{SANDBOX_URL}company/{companyID}/query"
        headers = {
            "Authorization": f"Bearer {accessToken}",
            "Accept": "application/json",
            "Content-Type": CONTENT_TYPE_TEXT
        }

        query = "SELECT * FROM SalesReceipt ORDERBY TxnDate DESC MAXRESULTS "+maxResults

        response = requests.get(url, headers=headers, params={"query": query})
        return response.json()