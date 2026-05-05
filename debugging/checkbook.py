class Checkbook:
    """
    Function description:
    Represents a simple checkbook system that allows deposits,
    withdrawals, and balance inquiries.

    Parameters:
    None

    Returns:
    None
    """
    def __init__(self):
        """
        Function description:
        Initializes the checkbook with a starting balance of 0.0.

        Parameters:
        None

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
        Adds the specified amount to the checkbook balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
        Subtracts the specified amount from the balance if sufficient funds exist.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
        Displays the current balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function description:
    Runs the checkbook application, allowing user interaction
    for deposits, withdrawals, balance checks, and exit.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
