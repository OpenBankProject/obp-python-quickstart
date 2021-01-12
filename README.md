# Example Account Creation in OBP

This script will create a **User** for OBP plus a bank **Customer** object for that User, and create an **Account** of a certain **Product** type.

See the obp_python folder for the individual python scripts calling the various OBP APIs. 

### Requirements:
The obp user configured in obp_python/config needs to be setup with the corresponding entitlements (roles) on sandbox side first.

You may want to use the CLI (https://github.com/OpenBankProject/OBP-CLI), the API Manager or API Explorer of your instance to grant the nessesary roles, else just use any REST client. 



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
