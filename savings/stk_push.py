import json

import requests
import base64
from datetime import datetime
from django.conf import settings
from .utils import get_mpesa_access_token


def stk_push(phone, amount, order_id):
    access_token = get_mpesa_access_token()
    if not access_token:
        return {"error": "failed to get mpesa access token"}

    timestamp = datetime.now().strftime('%Y%m%d%H')
    password = base64.b64encode(
        (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()).decode()

    payload = {

        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": f"Order_{order_id}",
        "TransactionDesc": "Payment for ordr",

    }
    headers = {"Authorization": f'{access_token}', 'Content-Type': 'application/json'}
    url = "https://sandbox.safaricom.c.ke/mpesa/stkpush/v1/processrequest"
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()
