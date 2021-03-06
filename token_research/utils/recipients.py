import os
from token_research.utils.accounts import backend


def generate_recipients(count):
    recipients = []
    while len(recipients) < count:
        address = backend.PrivateKey(os.urandom(32)).public_key.to_canonical_address()
        # aim for the worst case
        # zero in data costs 4 gas, non-zero byte is 68 gas
        if address.count(b'\x00') == 0:
            recipients.append(address)
    return recipients


def same_recipients(count):
    return [b'\x11' * 20 for _ in range(count)]
