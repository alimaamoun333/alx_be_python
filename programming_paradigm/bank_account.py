class BankAccount:
    """
    A simple bank account class that supports deposit, withdraw,
    and displaying the current balance.
    """

    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize the account with an optional starting balance.
        """
        self._account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Add the specified amount to the account balance.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self._account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Subtract the specified amount from the account if sufficient funds exist.
        Return True on success, False otherwise.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")
