from eth.utils.address import generate_contract_address

from token_research.utils import accounts


def deploy_contract(vm, bytecode):
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
