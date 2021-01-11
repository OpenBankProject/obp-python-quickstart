import logging
from .createDirectLoginToken import createDirectLoginToken


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("obp_python")
version = "v4.0.0"
verify = True
obp_api_host = "https://apisandbox.openbankproject.com"
username = "test_script32"
user_password = "Abjeef^blurarAwjooc6"
consumer_key = "c5twr2y5dsgjkbhcznr55sokgnv2zp5xpqkq4mnf"
bank_id = "our_test_bank"
obp_auth_token = createDirectLoginToken(username, user_password, consumer_key, obp_api_host, verify)

