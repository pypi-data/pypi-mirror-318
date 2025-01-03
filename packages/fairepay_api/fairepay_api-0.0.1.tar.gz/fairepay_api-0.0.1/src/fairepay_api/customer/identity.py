from json import dumps
import requests

from fairepay_api.customer.settings import ENDPOINT_CUSTOMER, ENDPOINT_CUSTOMER_IDENTITY


class CustomerIdentity:
    def __init__(self, authorize, endpoint):
        self.auth = authorize
        self.endpoint = endpoint

    def authorize(self):
        resp = requests.post(
            f"{self.endpoint}{ENDPOINT_CUSTOMER}{ENDPOINT_CUSTOMER_IDENTITY}/authorize",
            data=dumps(
                {
                    "client_id": self.auth.client_id,
                    "session_id": self.auth.session_id,
                    "hmac": self.auth.hmac_key,
                }
            ),
        )

        if resp.status_code != 200:
            print(resp.content)

        return resp.json()
