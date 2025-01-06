from easydict import EasyDict
from requests.auth import HTTPBasicAuth

from mecher_base_api_client.api_client import API


class BrowserStack_ApiCommon(API):
    def __init__(self, user_name: str, access_key: str):
        super().__init__(url='https://api-cloud.browserstack.com',
                         default_status_codes=(200, 201, 204),
                         timeout=100)
        self.auth = HTTPBasicAuth(username=user_name, password=access_key)

    def send_request(self, uri: str, **kwargs):
        if 'auth' not in kwargs:
            kwargs['auth'] = self.auth

        response = self.send_request_base(url=uri, **kwargs)
        return compound_list_to_easydict(response.json())
