from .config import obp_api_host, version
from .makeRequests import makePostRequest

def createBank(id=None, full_name=None, short_name=None,
                logo_url=None, website_url=None,
                bank_routing_scheme=None, bank_routing_address=None):

    payload = {
    "id": id,
    "short_name": short_name,
    "full_name": full_name,
    "logo": logo_url,
    "website": website_url,
    "bank_routings": [{
        "scheme": bank_routing_scheme,
        "address": bank_routing_address
        }]
    }
    url = obp_api_host + '/obp/{version}/banks'.format(version=version)

    return makePostRequest(url, payload)
