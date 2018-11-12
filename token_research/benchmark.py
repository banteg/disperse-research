from functools import partial

from eth.vm.forks.byzantium import ByzantiumVM
from eth.vm.forks.constantinople import ConstantinopleVM
from eth_utils import to_wei

from token_research.contracts.disperse import Disperse
from token_research.contracts.token import Token
from token_research.utils import accounts
from token_research.utils import binary_search
from token_research.utils.evm import EVM
from token_research.utils.recipients import generate_recipients


def main():
    vms = [ByzantiumVM, ConstantinopleVM]
    for vm_class in vms:
        evm = EVM(vm_class)
        print(evm.vm.fork)
        # load up the first 10 accounts with 100 ether each
        for n in range(1, 11):
            evm.set_balance(accounts.addr(n), to_wei(1, 'tether'))
        benchmark_token(evm)
        benchmark_disperse_ether(evm)
        benchmark_disperse_token(evm)


def benchmark_token(evm):
    token = Token(evm)
    value = to_wei(100, 'ether')
    address = accounts.addr(1)
    spender = accounts.addr(2)
    recipients = generate_recipients(2)
    token.set_balance(address, to_wei(1, 'kether'))
    token.approve(spender, 2 ** 256 - 1)

    for zero in ['zero', 'non-zero']:
        gas = token.transfer(recipients[0], value)
        print(f'token transfer, {zero} balance', gas)

    for zero in ['zero', 'non-zero']:
        gas = token.transferFrom(address, recipients[1], value, n=2)
        print(f'token transferFrom, {zero} balance', gas)


def benchmark_disperse_ether(evm):
    disperse = Disperse(evm)

    for have_balances in [False, True]:
        func = partial(disperse.estimate_ether, have_balances)
        label = ', '.join([
            'disperse ether',
            'non-zero balances' if have_balances else 'zero balances',
        ])
        num, gas = binary_search(func, label=label)
        print(
            label,
            f'{num} recipients, {gas} gas, {gas // num} gas/transfer',
            sep=', '
        )


def benchmark_disperse_token(evm):
    disperse = Disperse(evm)

    for simple in [True, False]:
        for have_balances in [False, True]:
            func = partial(disperse.estimate_token, have_balances, simple)
            label = ', '.join([
                'disperse token',
                'naive' if simple else 'optimized',
                'non-zero balances' if have_balances else 'zero balances',
            ])
            num, gas = binary_search(func, label=label)
            print(
                label,
                f'{num} recipients, {gas} gas, {gas // num} gas/transfer',
                sep=', '
            )


if __name__ == '__main__':
    main()
