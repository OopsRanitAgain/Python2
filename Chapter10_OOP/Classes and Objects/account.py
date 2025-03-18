from decimal import Decimal

class Account:
    def __init__(self,name,balance):
        if balance < Decimal('0.00'):
            raise ValueError('Balance must be Non-Negative')
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be Non-Negative')
        self.balance += amount

    def withdrawa(self,amount):
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be Positive')
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        self.balance -= amount
    
    def __repr__(self):
        return f'Account (name = {self.name!r}, Balance = {self.balance!r})'
    
    def __str__(self):
        return f'Account holder: {self.name}, Balance: {self.balance}'
    
    def __format__(self,format_spec):
        if format_spec == 'dollar':
            return f'Name : {self.name}, Balance: ${self.balance}'
        elif format_spec == 'rs':
            return f'Name : {self.name}, Balance: Rs {self.balance}'
        else:
            return f'{self.__str__() : {format_spec}}'
        