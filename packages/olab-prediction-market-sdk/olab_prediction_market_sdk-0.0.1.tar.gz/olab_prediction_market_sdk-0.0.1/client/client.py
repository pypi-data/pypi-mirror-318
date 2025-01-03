import logging
from datetime import time
from olab_open_api.olab_open_api.api import ApiClient
from olab_open_api.olab_open_api.api import open_api
from olab_open_api.olab_open_api.api import Configuration
from chain.contract_caller import ContractCaller
from chain.py_order_utils.builders import OrderBuilder
from python_sdk.chain.py_order_utils.model.order import OrderData
from types import SimpleNamespace

API_INTERNAL_ERROR_MSG = "Unable to process your request. Please contact technical support."
MISSING_MARKET_ID_MSG = "market_id is required."
MISSING_TOKEN_ID_MSG = "token_id is required."

class InvalidParamError(Exception):
    pass

class OpenApiError(Exception):
    pass

class Client:
    def __init__(self, host='', apikey='', private_key='', multi_sig_addr='', conditional_tokens_addr='', multisend_addr=''):
        self.conf = Configuration(host=host, api_key=apikey)
        self.contract_caller = ContractCaller(private_key=private_key, multi_sig_addr=multi_sig_addr,
                                              conditional_tokens_addr=conditional_tokens_addr,
                                              multisend_addr=multisend_addr)
        self.api_client = ApiClient(self.conf)
        self.api = open_api.OlabOpenApi(self.api_client)
        
    def get_currencies(self):
        thread = self.api.openapi_currency_get_with_http_info(self.conf.api_key)
        result = thread.get()
        return result