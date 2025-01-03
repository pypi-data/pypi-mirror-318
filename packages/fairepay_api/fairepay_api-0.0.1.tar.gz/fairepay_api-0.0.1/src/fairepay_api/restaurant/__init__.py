from fairepay_api.restaurant.orders import RestaurantOrders


class Restaurant:
    def __init__(self, authorize, endpoint):
        self.orders = RestaurantOrders(authorize=authorize, endpoint=endpoint)
