import requests

class VTPClient:
    def __init__(self, username=None, password=None, account_token=None, base_url=None):
        self.username = username
        self.password = password
        self.account_token = account_token
        self.base_url = base_url or "https://partnerdev.viettelpost.vn/v2/"
        self.token = None

        if not self.account_token:
            self.token = self.get_token_with_username_password()
        else:
            self.token = self.get_token_with_account_token()

    def get_token_with_username_password(self):
        """Retrieve token using username and password."""
        if not self.username or not self.password:
            raise ValueError("Username and password are required to get a token.")
        
        url = f"{self.base_url}user/Login"
        payload = {
            "USERNAME": self.username,
            "PASSWORD": self.password
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            response_json = response.json()
            if response_json.get("error"):
                raise ValueError("Failed to retrieve token, please provide valid credentials.")
            token = response.json().get("data", {}).get("token")
            if not token:
                raise ValueError("Failed to retrieve token from the response.")
            return token
        except requests.RequestException as e:
            raise Exception(f"Failed to retrieve token: {str(e)}")

    def get_token_with_account_token(self):
        """Retrieve token using account_token."""
        if not self.account_token:
            raise ValueError("Account token is required for this method.")
        url = f"{self.base_url}user/LoginVTP"
        payload = {
            "token": self.account_token
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            response_json = response.json()
            if response_json.get("error"):
                raise ValueError("Failed to retrieve token, please provide valid account token.")
            token = response.json().get("data", {}).get("token")
            if not token:
                raise ValueError("Failed to retrieve token.")
            return token
        except requests.RequestException as e:
            raise Exception(f"Failed to retrieve token: {str(e)}")

    def get_token(self):
        return self.token

    def _get_json_response(self, res):
        try:
            res.raise_for_status()
            return res.json()
        except requests.RequestException as e:
            raise Exception(f"Error while getting json response: {str(e)}")

    def make_request(self, url, method, data=None, params=None):
        headers ={
            "Content-Type": "application/json",
            "Token": self.token
        }
        if not self.token:
            raise ValueError("No token available. Provide valid credentials or account token.")
        try:
            if data:
                res = requests.request(method, url, json=data, headers=headers)
            else:
                res = requests.request(method, url, params=params, headers=headers)
            return self._get_json_response(res)
        except requests.RequestException as e:
            raise Exception(f"Error while making request: {str(e)}")
            
    def get_services(self, service_data):
        url = f"{self.base_url}order/getPriceAllNlp"
        return self.make_request(url, "POST", data=service_data)

    def charge_by_address(self, address_data):
        url = f"{self.base_url}order/getPriceNlp"
        return self.make_request(url, "POST", data=address_data)

    def create_order(self, order_data):
        url = f"{self.base_url}order/createOrderNlp"
        return self.make_request(url, "POST", data=order_data)
    
    def update_order(self, order_data):
        url = f"{self.base_url}order/edit"
        return self.make_request(url, "POST", data=order_data)

    def update_order_status(self, order_data):
        url = f"{self.base_url}order/UpdateOrder"
        return self.make_request(url, "POST", data=order_data)