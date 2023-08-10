import os

class CredentialUtility(object):

    def __init__(self):
        pass


    @staticmethod
    def get_woo_api_keys():
        wc_keys = os.environ.get("WOO_KEY")
        wc_secret = os.environ.get("WOO_SECRET")
        if not wc_keys or not wc_secret:
            raise Exception("The API credential 'WOO_KEY' AND 'WOO_SECRET' must be in env variables")

        else:
            return {'wc_keys': wc_keys, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The db credentials 'DB_USER' and 'DB_PASSWORD' must be in env variables")

        else:
            return {'db_user': db_user, 'db_password': db_password}
