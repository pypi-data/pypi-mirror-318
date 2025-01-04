from web3 import Web3
from eth_typing import ChecksumAddress
from typing import Any, Callable, Dict, List, Optional, Type, Union
from .enums import SafeOperationEnum
from chain.safe.constants import NULL_ADDRESS
from chain.safe.safe_tx import SafeTx
from functools import cached_property
from web3.types import BlockIdentifier, TxParams, Wei
from .safe_contracts.utils import get_safe_contract

VERSION = 'v1.3.0'


class Safe:
    def __init__(
            self,
            w3: Web3,
            address: ChecksumAddress,
    ):
        self.w3 = w3
        self.address = address
        self.contract = get_safe_contract(self.w3, self.address)

    @cached_property
    def chain_id(self) -> int:
        return self.w3.eth.chain_id

    def get_version(self) -> str:
        """
        :return: String with Safe Master Copy semantic version, must match `retrieve_version()`
        """
        return VERSION

    def retrieve_nonce(
            self, block_identifier: Optional[BlockIdentifier] = "latest"
    ) -> int:
        return self.contract.functions.nonce().call(
            block_identifier=block_identifier or "latest"
        )

    def build_multisig_tx(
            self,
            to: ChecksumAddress,
            value: int,
            data: bytes,
            operation: int = SafeOperationEnum.CALL.value,
            safe_tx_gas: int = 0,
            base_gas: int = 0,
            gas_price: int = 0,
            gas_token: ChecksumAddress = NULL_ADDRESS,
            refund_receiver: ChecksumAddress = NULL_ADDRESS,
            signatures: bytes = b"",
            safe_nonce: Optional[int] = None,
    ) -> SafeTx:
        """
        Allows to execute a Safe transaction confirmed by required number of owners and then pays the account
        that submitted the transaction. The fees are always transfered, even if the user transaction fails

        :param to: Destination address of Safe transaction
        :param value: Ether value of Safe transaction
        :param data: Data payload of Safe transaction
        :param operation: Operation type of Safe transaction
        :param safe_tx_gas: Gas that should be used for the Safe transaction
        :param base_gas: Gas costs for that are independent of the transaction execution
            (e.g. base transaction fee, signature check, payment of the refund)
        :param gas_price: Gas price that should be used for the payment calculation
        :param gas_token: Token address (or `0x000..000` if ETH) that is used for the payment
        :param refund_receiver: Address of receiver of gas payment (or `0x000..000` if tx.origin).
        :param signatures: Packed signature data ({bytes32 r}{bytes32 s}{uint8 v})
        :param safe_nonce: Nonce of the safe (to calculate hash)
        :return: SafeTx
        """

        if safe_nonce is None:
            safe_nonce = self.retrieve_nonce()
        return SafeTx(
            self.w3,
            self.address,
            to,
            value,
            data,
            operation,
            safe_tx_gas,
            base_gas,
            gas_price,
            gas_token,
            refund_receiver,
            signatures=signatures,
            safe_nonce=safe_nonce,
            safe_version=self.get_version(),
            chain_id=self.chain_id,
        )
