# CRM Module VTP

A CRM module for VTP.

## Installation

You can install the package using pip:

```bash
pip install crm_module_vtp
```


## Usage

### Initialize the Client

You can initialize the client using either a username and password or an account token.

#### Using Username and Password

```
from crm_module_vtp.client import VTPClient
VTPclient = VTPClient(username="your_username", password="your_password")
token = VTPclient.get_token()
```

#### Using Account Token

```
from crm_module_vtp.client import VTPClient
VTPclient = VTPClient(account_token="your_account_token")
token = VTPclient.get_token()
```

### Get Services

You can use the client to get services by providing the necessary service data.

```
service_data = {
    "SENDER_ADDRESS": "Đại Mỗ, Nam Từ Liêm, Hà Nội",
    "RECEIVER_ADDRESS": "Định Công, Hoàng Mai, Hà Nội",
    "RECEIVER_PROVINCE": 1,
    "PRODUCT_TYPE": "HH",
    "PRODUCT_WEIGHT": 100,
    "PRODUCT_PRICE": 5000000,
    "MONEY_COLLECTION": "5000000",
    "PRODUCT_LENGTH": 0,
    "PRODUCT_WIDTH": 0,
    "PRODUCT_HEIGHT": 0,
    "TYPE": 1,
}
response = VTPclient.get_services(service_data)
```
