class Account:
    def __init__(self, username, initial_balance, account_number):
        self.username = username
        self.initial_balance = initial_balance
        self.account_number = account_number
        self.transactions = []

    def current_balance(self):
        return self.initial_balance

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions
