from eth.exceptions import VMError
from eth_utils import to_wei

from token_research.utils.accounts import addr
from token_research.contracts.token import Token
from token_research.utils import Contract
from token_research.utils.recipients import generate_recipients


class StormSender(Contract):

    name = 'UpgradebleStormSender'

    def __init__(self, evm):
        self.evm = evm
        super().__init__(evm.vm)
        self.deploy(self.name)
        self.initialize()

    def initialize(self):
        return self.transact('initialize(address)', [addr(1)])

    def estimate_token(self, have_balances: bool, simple: bool, count: int):
        value = to_wei(100, 'ether')
        recipients = generate_recipients(count)
        values = [value for _ in recipients]

        token = Token(self.evm)
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

            for address in recipients:
                assert self.vm.state.account_db.get_balance(address) == value

        try:
            return self.disperse_ether(recipients, values)
        except VMError:
            return

    def disperse_token(self, token, recipients, values, simple=False):
        name = 'multisendToken(address,address[],uint256[])'
        return self.transact(name, [token.address, recipients, values], value=to_wei(50, 'finney'))

    def disperse_ether(self, recipients, values):
        name = 'multisendEther(address[],uint256[])'
        return self.transact(name, [recipients, values], value=sum(values) + to_wei(50, 'finney'))
