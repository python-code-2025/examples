class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    # Public method to deposit funds
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Getter to access the private balance
    def get_balance(self):
        return self.__balance


# Subclass CheckingAccount inheriting from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)

    # Method to access parent's private balance using the getter
    def check_balance(self):
        balance = self.get_balance()  # Access the private attribute via the getter
        print(f"Checking Account balance is: {balance}")


# Example usage:
account1 = CheckingAccount(1000)
account1.deposit(500)  # Deposit into the checking account
account1.check_balance()  # Accessing the balance using the getter
