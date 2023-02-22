# Bank-account-program
OPP challenge from The Complete Python Bootcamp: From zero to Hero (Jose Portilla) extended for a new functionalities.

Includes a CurrencyRates base class to have a exchange rates valid all the time.

Attributes:
self.owner = owner  -> account owner
self.balance = balance -> available founds on your account 
self.currency = '$ -> your account currency ($ by default) 
self.c = CurrencyRates() -> gives current rate of currencies from forex
self.USD_GBP = round(self.c.get_rate('USD', 'GBP'), 2) -> current USD/GBP rate
self.USD_EUR = round(self.c.get_rate('USD', 'EUR'), 2) -> current USD/EUR rate
self.USD_PLN = round(self.c.get_rate('USD', 'PLN'), 2) -> current USD/PLN rate
self.currency_dict -> store currencies (names and their rates) as a dict, realtime values



Methods:
def deposit(self, amount) -> allows to deposit a money on your account (part of the course challenge),

def withdraw(self, amount) -> allows to withdraw a money from your account. 
Remember that you cannot withdraw more money then you own. (part of the course challenge)

def check_balance(self) -> to check how much money you have on your account (additional functionality, I've added)

def change_currency(self) -> you can change the currency of your account. 
The value of balance will change accourding to the current currency rate. Also currency_dict refresh its values. Only four currencies to choose (additional functionality, I've added).

def show_exchange_rates(self) -> you can see what is the current exchange rates.


