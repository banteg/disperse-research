from eth_keys import KeyAPI

backend = KeyAPI()
accounts = {}


def priv(n: int):
    if n not in accounts:
        accounts[n] = backend.PrivateKey(n.to_bytes(32, 'big'))
    return accounts[n]


def addr(n: int):
    return priv(n).public_key.to_canonical_address()


def pair(n: int):
    return addr(n), priv(n)
