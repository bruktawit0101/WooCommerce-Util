import os
from CredentialUtility import CredentialUtility
from woocommerce import API



class WooCommerceUtility(object):

    def __init__(self):
        woo_creds = CredentialUtility().get_woo_api_keys()

        base_url = os.environ.get('BASE_URL')

        self.wcapi = API(
            url=base_url,
            consumer_key=woo_creds['wc_keys'],
            consumer_secret=woo_creds['wc_secret'],
            version="wc/v3",
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"if bad status code."\
          f"Expected {self.expected_status_code}, Actual status code: {self.status_code},"\
          f"URL: {self.url}, Response Json: {self.rs_json}"

    def get(self, woo_endpoint, params=None, return_headers=False, expected_status_code=200):
        rs_api = self.wcapi.get(woo_endpoint, params=params)
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.status_code = rs_api.status_code
        self.url = rs_api.url
        if return_headers:
            return {'response_json': self.rs_json, 'headers': rs_api.headers}
        else:
            return self.rs_json
    def delete(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.delete(wc_endpoint, params=params)
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.status_code = rs_api.status_code
        self.url = rs_api.url
        return self.rs_json
if __name__ == '__main__':
    obj = WooCommerceUtility()
    rs_api = obj.get('products')
    print(rs_api)








