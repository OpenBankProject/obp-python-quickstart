import requests
from .config import obp_auth_token, logger, verify

authorization = 'DirectLogin token="{}"'.format(obp_auth_token)
headers = {'Content-Type': 'application/json',
           'Authorization': authorization}


def check400status(req):
    if req.status_code >= 400:
        logger.error("Request: " + req.url + " has bad result, code: " + str(req.status_code))
        logger.error(req.text)
    else:
        logger.debug("Result for request: " + req.url + " :")
        logger.debug(req.status_code)
        logger.debug(req.text)
    return req


def makeGetRequest(url):
    req = requests.get(url, headers=headers, verify=verify)
    return check400status(req)


def makePutRequest(url,payload):
    req = requests.put(url, headers=headers, json=payload, verify=verify)
    return check400status(req)


def makePostRequest(url,payload):
    req = requests.post(url, headers=headers, json=payload, verify=verify)
    return check400status(req)

def makeDeleteRequest(url):
    req = requests.delete(url, headers=headers, verify=verify)
    return check400status(req)
