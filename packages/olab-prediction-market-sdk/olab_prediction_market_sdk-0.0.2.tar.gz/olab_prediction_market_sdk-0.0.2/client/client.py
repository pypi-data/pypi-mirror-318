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
    
    
    #   def get_markets(self):
    #     response = self.api.openapi_topic_get_with_http_info(self.conf.api_key)
    #     return response
    
    # def get_market(self, market_id):
    #     try:
    #         if not market_id:
    #             raise InvalidParamError(MISSING_MARKET_ID_MSG)
            
    #         response = self.api.openapi_topic_topic_id_get_with_http_info(self.conf.api_key, market_id)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get market: {e}")
    
    # def get_categorical_market(self, market_id):
    #     try:
    #         if not market_id:
    #             raise InvalidParamError(MISSING_MARKET_ID_MSG)
            
    #         response = self.api.openapi_topic_multi_topic_id_get(self.conf.api_key, market_id)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get categorical market: {e}")
    
    # def get_candles(self, token_id, interval="1hour", start_time=int(time.time()), bars=60):
    #     try:
    #         if not token_id:
    #             raise InvalidParamError(MISSING_TOKEN_ID_MSG)
            
    #         if not interval:
    #             raise InvalidParamError('interval is required')
                
    #         response = self.api.openapi_order_kline_get(self.conf.api_key, token_id, interval, start_time, bars)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get candles: {e}")
    
    # def get_orderbook(self, token_id):
    #     try:
    #         if not token_id:
    #             raise InvalidParamError(MISSING_TOKEN_ID_MSG)
            
    #         response = self.api.openapi_orderbook_get(self.conf.api_key, token_id)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get orderbook: {e}")
    
    # def get_depth(self, token_id, limit=10):
    #     try:
    #         if not token_id:
    #             raise InvalidParamError(MISSING_TOKEN_ID_MSG)
            
    #         response = self.api.openapi_depth_get(self.conf.api_key, token_id, limit)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get depth: {e}")
        
    # def place_order(self, data: OrderData, exchange_addr='', chain_id=8453):
    #     try:
    #         if not exchange_addr:
    #             raise InvalidParamError('exchange_addr is required')
    #         if not chain_id:
    #             raise InvalidParamError('chain_id is required')
            
    #         builder = OrderBuilder(exchange_addr, chain_id, self.contract_caller.signer)
    #         order = builder.build_order(data)
    #         signerOrder = builder.build_signed_order(order)
            
    #         v2_api = open_api(self.api_client)

    #         response = v2_api.openapi_order_post(self.conf.api_key, v2_add_order_req=signerOrder)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to place order: {e}")
    
    # def cancel_order(self, trans_no=0):
    #     if not trans_no or not isinstance(trans_no, int):
    #         raise InvalidParamError('trans_no is required and must be an integer')
        
    #     v2_api = open_api(self.api_client)
        
    #     response = v2_api.openapi_order_cancel_order_post(self.conf.api_key, view_cancel_order_request=SimpleNamespace(trans_no))
    #     return response
    
    # def get_my_open_orders(self, market_id=0, limit=10):
    #     try:
    #         if not isinstance(market_id, int):
    #             raise InvalidParamError('market_id must be an integer')
            
    #         response = self.api.openapi_order_get(self.conf.api_key, market_id, limit)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get open orders: {e}")
    
    # def get_my_positions(self, market_id=0, page=1, pageSize=10):
    #     try: 
    #         if not isinstance(market_id, int):
    #             raise InvalidParamError('market_id must be an integer')
            
    #         if not isinstance(page, int):
    #             raise InvalidParamError('page must be an integer')
            
    #         if not isinstance(pageSize, int):
    #             raise InvalidParamError('pageSize must be an integer')
            
            
    #         response = self.api.openapi_portfolio_get(self.conf.api_key, market_id, page, pageSize)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get my positions: {e}")
    
    # def get_my_balances(self):
    #     try:
    #         response = self.api.openapi_balance_get(self.conf.api_key)
    #         return response
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get my balances: {e}")
        
    #     return response
    
    # def get_my_trades(self, market_id=0, limit=10):
    #     try:
    #         if not isinstance(market_id, int):
    #             raise InvalidParamError('market_id must be an integer')
            
    #         response = self.api.openapi_trade_get(self.conf.api_key, market_id, limit)
    #         return response
    #     except InvalidParamError as e:
    #         logging.error(f"Validation error: {e}")
    #         raise
    #     except Exception as e:
    #         logging.error(f"API error: {e}")
    #         raise OpenApiError(f"Failed to get my trades: {e}")

    # def connect_socket():
    #     pass
    
    # def on_new_trade(listener):
    #     pass
    
    # def on_orderbook_change(listener):
    #     pass
    
    