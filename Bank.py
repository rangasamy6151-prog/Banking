class Account:
    def __init__(self, acc_number, name, acc_type, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {amount} deposited successfully.")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(" Insufficient balance!")
        else:
            self.balance -= amount
            print(f" {amount} withdrawn successfully.")

    def display_account(self):
        print("\n Account Details")
        print(f"Account Number: {self.acc_number}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_number = input("Enter Account Number: ")
        if acc_number in self.accounts:
            print(" Account number already exists.")
            return
        name = input("Enter Account Holder Name: ").capitalize()
        acc_type = input("Enter Account Type (Savings/Current): ").capitalize()
        balance = int(input("Enter Initial Deposit: "))
        self.accounts[acc_number] = Account(acc_number, name, acc_type, balance)
        print(" Account created successfully.")

    def deposit_money(self):
        acc_number = input("Enter Account Number: ")
        account = self.accounts.get(acc_number)
        if account:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print(" Account not found.")

    def withdraw_money(self):
        acc_number = input("Enter Account Number: ")
        account = self.accounts.get(acc_number)
        if account:
            amount = int(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print(" Account not found.")

    def check_balance(self):
        acc_number = input("Enter Account Number: ")
        account = self.accounts.get(acc_number)
        if account:
            print(f" Current Balance: ₹{account.balance}")
        else:
            print(" Account not found.")

    def view_account_details(self):
        acc_number = input("Enter Account Number: ")
        account = self.accounts.get(acc_number)
        if account:
            account.display_account()
        else:
            print(" Account not found.")
bank = Bank()
def main():
    
    while True:
        print("\n====== Bank Management System ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            bank.view_account_details()
        elif choice == '6':
            print(" Thank you for using the Bank Management System!")
            break
        else:
            print(" Invalid choice, please try again.")
main()
