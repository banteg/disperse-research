from eth_abi import encode_abi
from eth_utils import to_int, keccak


def mapping(typ, key, value):
    return to_int(keccak(encode_abi([typ, 'uint256'], [key, value])))


def balances(address):
    return mapping('address', address, 0)


def allowed(address, spender):
    return mapping('address', spender, mapping('address', address, 1))
