class Account:
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        return "Interest calculated for savings account"

class CurrentAccount(Account):
    def calculate_interest(self):
        return "Interest calculated for current account"