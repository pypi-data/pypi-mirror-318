import requests
import os

from fairepay_api.restaurant.settings import (
    ENDPOINT_RESTAURANT,
    ENDPOINT_RESTAURANT_ORDERS,
)


class RestaurantOrders:
    def __init__(self, authorize, endpoint):
        self.authorize = authorize
        self.endpoint = endpoint

    def get_orders(self):
        resp = requests.get(
            f"{self.endpoint}{ENDPOINT_RESTAURANT}{ENDPOINT_RESTAURANT_ORDERS}",
            headers={"language": "da"},
            params={
                "client_id": self.authorize.client_id,
                "session_id": self.authorize.session_id,
                "hmac_key": self.authorize.hmac_key,
            },
        )

        if resp.status_code != 200:
            print(resp.content)

        return {"status": "OK"}
