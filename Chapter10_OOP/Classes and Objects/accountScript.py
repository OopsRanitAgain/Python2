from account import Account
from decimal import Decimal

account1 = Account('Ranit',Decimal('100.00'))
print(account1.balance)

account1.balance = Decimal('-1000')
print(account1.balance)