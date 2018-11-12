from eth.exceptions import VMError
from eth_utils import from_wei, to_int, to_wei

from token_research.utils import Contract, accounts
from token_research.utils import storage
from token_research.utils.recipients import generate_recipients

from token_research.contracts.token import Token


class Disperse(Contract):

    def __init__(self, evm):
        super().__init__(evm.vm)
        self.deploy('Disperse')

    def estimate_token(self, have_balances: bool, count: int, simple: bool):
        value = to_wei(100, 'ether')
        recipients = generate_recipients(count)
        values = [value for _ in recipients]

        token = Token(self.vm)
        token.approve(self.address, 2 ** 256 - 1)

        if have_balances:
            for address in recipients:
                token.set_balance(address, value)

        try:
            return self.disperse_token(token, recipients, values, simple)
        except VMError:
            return

    def estimate_ether(self, have_balances: bool, count: int):
        value = to_wei(1, 'ether')
        recipients = generate_recipients(count)
        values = [value for _ in recipients]

        if have_balances:
            for address in recipients:
                self.vm.state.account_db.set_balance(address, value)
            self.vm.state.account_db.persist()

        try:
            return self.disperse_ether(recipients, values)
        except VMError:
            return

    def disperse_token(self, token, recipients, values, simple=False):
        name = 'disperseTokenSimple' if simple else 'disperseToken'
        func = f'{name}(address,address[],uint256[])'
        return self.transact(func, [token.address, recipients, values])

    def disperse_ether(self, recipients, values):
        return self.transact('disperseEther(address[],uint256[])', [recipients, values], value=sum(values))
