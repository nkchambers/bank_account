class BankAccount:

    accounts = []

    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)


    def deposit(self, amount):
        self.account_balance += amount

        return self


    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
        else:
            print ('Insufficient Funds: Charging $5.00 Fee')
            self.account_balance -= 5

        return self
    
    @staticmethod
    def can_withdraw(account_balance, amount):
        if (account_balance - amount) < 0:
            return False
        else:
            return True


    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")

        return self


    def yield_interest(self):
        if BankAccount.can_yield_int(self.account_balance):
            self.account_balance += (self.account_balance * self.int_rate)
        else:
            print('Insufficient Funds')
        return self
    
    @staticmethod 
    def can_yield_int(account_balance):
        if account_balance < 0:
            return False
        else:
            return True

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()




# Instantiate Bank Accounts - Create 2 Accounts
nick = BankAccount (int_rate = 0.01, account_balance = 500)
wayne = BankAccount (int_rate = 0.01, account_balance = 0)
russell = BankAccount(int_rate = 0.01, account_balance = 20000)


nick.deposit(600).deposit(700).withdraw(200).yield_interest()
wayne.deposit(5000000).deposit(5000000).deposit(9000000).withdraw(3000000).yield_interest()
russell.deposit(500000).deposit(700000).withdraw(100000).withdraw(50000).withdraw(50000).withdraw(200000).yield_interest()

BankAccount.print_all_accounts()