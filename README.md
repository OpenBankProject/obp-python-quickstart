# Example Account Creation in OBP

This script will create a user for obp plus bank customer object for that user, and create an account of a certain (product)type.
### Requirements:
The obp user configured in obp_python/config needs to be setup with the corresponding entitlements(roles) on sandbox side first



### Run:
change the following global variables in full_flow_up_to_create_account.py unless the script is run for the very first time
t:
```
user_name_to_create = "some_user_name"
product_code = "some_myproduct_name"
product_attribute_name = "some_product_feature"
product_attribute_value = "some+product_feature_value"
```
then just run it: 
```
python3 ./full_flow_up_to_create_account.py
```