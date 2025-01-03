from enum import Enum


class AuthorizeType(Enum):
    CUSTOMER = "customer"


class Authorize:
    def __init__(
        self,
        type: AuthorizeType,
        client_id: str = None,
        session_id: str = None,
        hmac_key: str = None,
    ):
        self.client_id = None
        self.session_id = None
        self.hmac_key = None

        if type == AuthorizeType.CUSTOMER:
            self.auth_type_customer(
                client_id=client_id, session_id=session_id, hmac_key=hmac_key
            )

        else:
            raise ValueError("Uknowing AuthorizeType")

    def auth_type_customer(self, client_id: str, session_id: str, hmac_key: str):
        self.client_id = client_id
        self.session_id = session_id
        self.hmac_key = hmac_key
