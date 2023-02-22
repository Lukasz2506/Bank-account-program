from forex_python.converter import CurrencyRates


class Bank(CurrencyRates):

    def __init__(self, owner, balance=0):
        CurrencyRates.__init__(self)
        self.owner = owner
        self.balance = balance
        self.currency = '$'
        self.c = CurrencyRates()
        self.USD_GBP = round(self.c.get_rate('USD', 'GBP'), 2)
        self.USD_EUR = round(self.c.get_rate('USD', 'EUR'), 2)
        self.USD_PLN = round(self.c.get_rate('USD', 'PLN'), 2)
        self.currency_dict = {'$': 1, ' \N{pound sign}': self.USD_GBP, '\N{euro sign}': self.USD_EUR,
                              'PLN': self.USD_PLN}

    def __str__(self):
        return f'This account belongs to {self.owner}\nYour founds: {self.balance}{self.currency}'

    def deposit(self, amount):
        self.balance += amount
        print(f'The founds was added successfully: {amount}{self.currency}')

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            print(f'withdrawing in progress...')
            self.balance -= amount
            print(f'here is your {self.currency}')
        else:
            print(f'Sorry, not enough {self.currency}')

    def check_balance(self):
        print(f'your current balance is {self.balance}{self.currency}')

    def change_currency(self):
        # Allows to change the currency in your account.
        new_currency = input(f'your current currency is {self.currency}. '
                             f'\nPlease choose the currency you would like to change for \
                             \n($, \N{pound sign}, \N{euro sign}, PLN): >')
        if new_currency in self.currency_dict:
            rate = self.currency_dict[new_currency]
            self.balance *= rate
            for key in self.currency_dict:
                self.currency_dict[key] = round(self.currency_dict[key] / rate, 2)
            print(f'The currency was changed successfully from {self.currency} to {new_currency}')
            self.currency = new_currency

    def show_exchange_rates(self):
        # Show currencies rate.
        print(self.currency_dict)



