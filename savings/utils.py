import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


def get_mpesa_access_token():
    url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    if response.status_code == 200:
        return response.json().get("access_token")
    return None
