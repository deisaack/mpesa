import requests
from requests.auth import HTTPBasicAuth
#
# consumer_key = "060pCEKpfAe6vT7wKvhxdIPSA8EdrzBd"
# consumer_secret = "ZbAqffAgxqE8sTjR"
# api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#
# r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
# r = r.text
# print(r)
#
# import pympesa
#
# response = pympesa.oauth_generate_token(
#     consumer_key, consumer_secret).json()
# access_token = response.get("access_token")
# print(access_token)

# from pympesa import Pympesa
#
# import requests

access_token = "xlTTAVmRdz995NigZxC3G9HwgGY7"
import requests
#
# url="http://d20a6b30.ngrok.io/f/mpesa/"
# api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
# headers = {"Authorization": "Bearer %s" % access_token}
# request = { "ShortCode": "600337",
#     "ResponseType": "application/json",
#     "ConfirmationURL": url,
#     "ValidationURL": url}

import requests

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode":"600337",
  "CommandID":"CustomerPayBillOnline",
  "Amount":"600",
  "Msisdn":"254708374149",
  "BillRefNumber":"testapi0337" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)

# response = requests.post(api_url, json = request, headers=headers)
#
# print (response.text)
# url="http://d20a6b30.ngrok.io/ipn/mpesa/"
# api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
# headers = {"Authorization": "Bearer %s" % access_token}
# request = {
#             "ShortCode": "600337",
#             "ValidationURL": url
#            }
# request = { "ShortCode": "600337",
#     "ResponseType": "application/json",
#     "ConfirmationURL": url,
#     "ValidationURL": url}

# response = requests.post(api_url, json = request, headers=headers)

# print (response.text)
# mpesa_client = Pympesa(access_token)
# mpesa_client.c2b_register_url(
#     ValidationURL="http://d20a6b30.ngrok.io/saf/",
#     ConfirmationURL="http://d20a6b30.ngrok.io/saf/",
#     ResponseType="Completed",
#     ShortCode="01234"
#     )
#
# mpesa_client.lipa_na_mpesa_online_payment(
#     BusinessShortCode="600000",
#     Password="xxxxx_yyyy_zzz",
#     TransactionType="CustomerPayBillOnline",
#     Amount="100",
#     PartyA="254708374149",
#     PartyB="600000",
#     PhoneNumber="254708374149",
#     CallBackURL="https://your-app/callback",
#     AccountReference="ref-001",
#     TransactionDesc="desc-001"
#     )
#
# access_token = "eYmfEp0JSGST9QRAMDhV4tdOGQ2r"
# api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
# headers = {"Authorization": "Bearer %s" % access_token}
# request = { "ShortCode": "600337",
#     "ResponseType": "application/json",
#     "ConfirmationURL": "http://c185fba2.ngrok.io/saf/",
#     "ValidationURL": "http://c185fba2.ngrok.io/saf/"}
#
# print(request)
# print(headers)
#
# response = requests.post(api_url, json = request, headers=headers)
#
# print (response.text)
# curl -X POST --header "Content-Type: application/json" --header "Authorization: Bearer xlTTAVmRdz995NigZxC3G9HwgGY7" -d "{
#     \"ShortCode\": \"600337 \" ,
#     \"CommandID\": \"CustomerPayBillOnline\",
#     \"Amount\": \"100\",
#     \"Msisdn\": \"254708374149\",
#     \"BillRefNumber\": \"y\"
#     \"ConfirmationURL\": \"http://d20a6b30.ngrok.io/f/mpesa/\",
#     \"ValidationURL\": \"http://d20a6b30.ngrok.io/f/mpesa/\"
# }" "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
#
# # curl -X POST --header "Content-Type: application/json" --header "Authorization: Bearer iLTJjA6CUSZZRGfO9ftQCkNhhdLc" -d "{
#     \"ShortCode\": \"600337\",
#     \"CommandID\": \"CustomerPayBillOnline\",
#     \"Amount\": \"100\",
#     \"Msisdn\": \"254708374149\",
#     \"BillRefNumber\": \"y\"
# }" "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
