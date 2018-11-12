import json

from eth.utils.address import generate_contract_address
from eth_utils import to_bytes

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


def deploy_artifact(vm, name: str):
    artifact = json.load(open(f'artifacts/truffle/{name}.json'))
    bytecode = to_bytes(hexstr=artifact['bytecode'])
    return deploy_contract(vm, bytecode)
