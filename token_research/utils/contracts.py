import json
import re

from eth.utils.address import generate_contract_address
from eth_abi import encode_abi
from eth_utils import to_bytes, keccak

from token_research.utils import accounts


def deploy_contract(vm, bytecode: bytes):
    sender, priv = accounts.pair(1)
    nonce = vm.state.account_db.get_nonce(sender)
    contract = generate_contract_address(sender, nonce)
    tx = vm.create_unsigned_transaction(
        nonce=nonce,
        gas_price=1,
        gas=3141592,
        to=b'',
        value=0,
        data=bytecode,
    ).as_signed_transaction(priv)
    vm.state.apply_transaction(tx)
    return contract


def call_data(function: str, *params):
    name, types = re.search(r'(.*)\((.*)\)', function).groups()
    return keccak(function.encode())[:4] + encode_abi(types.split(','), params)


class Contract:

    def __init__(self, vm):
        self.vm = vm

    def deploy(self, name: str):
        artifact = json.load(open(f'artifacts/truffle/{name}.json'))
        bytecode = to_bytes(hexstr=artifact['bytecode'])
        self.address = deploy_contract(self.vm, bytecode)
        return self.address

    def call(self, function, params):
        data = call_data(function, *params)
        addr, priv = accounts.pair(1)
        tx = self.vm.create_unsigned_transaction(
            to=self.address, data=data, nonce=0, gas_price=1, gas=8000000, value=0
        ).as_signed_transaction(priv)
        result = self.vm.state.costless_execute_transaction(tx)
        return result

    def transact(self, function, params, value=0, n=1):
        data = call_data(function, *params)
        addr, priv = accounts.pair(n)
        nonce = self.vm.state.account_db.get_nonce(addr)
        tx = self.vm.create_unsigned_transaction(
            to=self.address, data=data, nonce=nonce, gas_price=1, gas=8000000, value=value
        ).as_signed_transaction(priv)
        root, computation = self.vm.state.apply_transaction(tx)
        computation.raise_if_error()
        gas_used = tx.gas - computation._gas_meter.gas_remaining
        return gas_used
