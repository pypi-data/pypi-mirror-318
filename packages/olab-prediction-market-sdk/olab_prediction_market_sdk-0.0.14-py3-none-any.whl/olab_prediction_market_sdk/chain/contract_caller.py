from ..chain.py_order_utils.signer import Signer
class ContractCaller:
    def __init__(self, private_key='', multi_sig_addr='', conditional_tokens_addr='', multisend_addr=''):
        self.private_key = private_key
        self.multi_sig_addr = multi_sig_addr
        self.conditional_tokens_addr = conditional_tokens_addr
        self.multisend_addr = multisend_addr
        self.signer = Signer(self.private_key)