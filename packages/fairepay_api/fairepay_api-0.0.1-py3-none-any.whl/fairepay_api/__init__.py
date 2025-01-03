from fairepay_api.authorize import Authorize, AuthorizeType
from fairepay_api.customer import Customer
from fairepay_api.restaurant import Restaurant
from fairepay_api.settings import SERVICE_ENDPOINT


class FPService:
    def __init__(
        self,
        authorize: Authorize,
        endpoint: str = None,
    ):
        self.service_endpoint = endpoint if endpoint is not None else SERVICE_ENDPOINT
        self.service_authorize = authorize

        self.customer = Customer(
            authorize=self.service_authorize, endpoint=self.service_endpoint
        )
        self.restaurant = Restaurant(
            authorize=self.service_authorize, endpoint=self.service_endpoint
        )
