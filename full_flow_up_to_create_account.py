from obp_python.createUser import createUser
from obp_python.createCustomer import createCustomer
from obp_python.linkUserToCustomer import linkUserToCustomer
from obp_python.createProduct import createProduct
from obp_python.createProductAttribute import createProductAttribute
from obp_python.createAccountApplication import createAccountApplication
from obp_python.createAccount import createAccount
from obp_python.config import logger, bank_id
from json import loads
from uuid import uuid4


user_name_to_create = "some_user_name"
product_code = "some_myproduct_name"
product_attribute_name = "some_product_feature"
product_attribute_value = "some+product_feature_value"
try:
	print("creating OBP user: ")
	res = createUser(user_name_to_create, user_name_to_create + "@testuser.com", "thisislongerthansixteen", "hans", user_name_to_create)
	user_one_id = loads(res.text)["user_id"]
	print(res.text)
except Exception as e:
	logger.exception("could not create user: " + user_name_to_create + ": " + str(e))
	exit(1)

try:
	print("creating Bank customer for OBP user")
	res = createCustomer(
		bank_id=bank_id,
		legal_name="hans " + user_name_to_create,
		mobile_phone_number="421432143214132",
		email="user_one@testuser.com",
		face_image_url="none",
		face_image_date="2017-09-19T00:00:00Z",
		date_of_birth="2000-09-19T00:00:00Z",
		relationship_status="single",
		dependants=1,
		dob_dependants=["2017-09-19T00:00:00Z"],
		credit_rating_rating="AAA",
		credit_rating_source="obp",
		credit_limit_currency="EUR",
		credit_limit_amount=10000,
		highest_education_attained="b.sc.",
		employment_status="employed",
		kyc_status=True,
		last_ok_date="2020-09-19T00:00:00Z",
		title="Mr.",
		branch_id="None",
		name_suffix=""
	)
	customer_one_id = loads(res.text)["customer_id"]
	print(res.text)
except:
	logger.exception("could not create customer_one")
	exit(1)

try:
	print("link the OBP user to the Bank customer: ")
	res = linkUserToCustomer(bank_id, user_one_id, customer_one_id)
	print(res.text)
except Exception as e:
	print("Could not link user " + user_one_id + " to customer " + customer_one_id)

try:
	print("creating product " + product_code + ": ")
	res = createProduct(
		bank_id=bank_id,
		product_code=product_code,
		parent_product_code="",
		category="None",
		family="None",
		superfamily="None",
		more_info_url="None",
		details="mydetails",
		description="mydescription",
		license_id="None",
		license_name="None"
	)
	print(res.text)
except Exception as e:
	logger.exception("could not create Product: " + str(e))
	exit(1)

try:
	print("create bank specific custom product attribute: ")
	res = createProductAttribute(
		bank_id=bank_id,
		product_code=product_code,
		name=product_attribute_name,
		_type="STRING",
		value=str(product_attribute_value)
	)
	print(res.text)
except Exception as e:
	logger.exception("could not create product attribute: " + str(e))
	exit(1)

try:
	print("creating account application: ")
	res = createAccountApplication(bank_id, user_one_id, customer_one_id, product_code)
	print(res.text)
except Exception as e:
	print("could not create acccount application: " + str(e))

try:
	print("creating account")
	res = createAccount(
		bankid=bank_id,
		userid=user_one_id,
		currency="EUR",
		label="label",
		productcode=product_code,
		branchid="None",
		accountrouting_scheme="UUID",
		accountrouting_address=str(uuid4())
	)
	user_one_account_id = loads(res.text)["account_id"]
	print(res.text)
except Exception as e:
	logger.exception("could not create account for user one: " + str(e))
	exit(1)

