from fairepay_api.customer.orders import CustomerOrders
from fairepay_api.customer.identity import CustomerIdentity


class Customer:
    def __init__(self, authorize, endpoint):
        self.orders = CustomerOrders(authorize=authorize, endpoint=endpoint)
        self.identity = CustomerIdentity(authorize=authorize, endpoint=endpoint)
