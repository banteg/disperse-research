from eth_utils import to_int

from token_research.utils import Contract
from token_research.utils import storage


class Token(Contract):

    def __init__(self, vm):
        super().__init__(vm)
        self.deploy('Token')

    def balance_of(self, address):
        result = self.call('balanceOf(address)', [address])
        return to_int(result.output)

    def set_balance(self, address, value):
        key = storage.balances(address)
        self.vm.state.account_db.set_storage(self.address, key, value)
        self.vm.state.account_db.persist()

    def allowance(self, address, spender):
        result = self.call('allowance(address,address)', [address, spender])
        return to_int(result.output)

    def approve(self, spender, value, n=1):
        result = self.transact('approve(address,uint256)', [spender, value], n=n)
        return result
