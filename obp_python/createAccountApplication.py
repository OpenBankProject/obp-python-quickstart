from .makeRequests import makePostRequest
from .config import obp_api_host


def createAccountApplication(bankid=None, userid=None, customerid=None, productcode=None):

  payload = {
    "product_code": productcode,
    "user_id": userid,
    "customer_id": customerid
}

  url = obp_api_host + '/obp/v4.0.0/banks/{BANK_ID}/account-applications'.format(BANK_ID=bankid)
  
  return makePostRequest(url,payload)
