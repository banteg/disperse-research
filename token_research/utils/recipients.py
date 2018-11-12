from token_research.utils import accounts


def generate_recipients(count):
    recipients = []
    n = 100
    while len(recipients) < count:
        n += 1
        address = accounts.addr(n)
        # data field: zero = 4 gas, non-zero = 68 gas, aim for the worst case
        if address.count(b'\x00') == 0:
            recipients.append(address)
    return recipients


def same_recipients(count):
    return [b'\x11' * 20 for _ in range(count)]
