cash_now = 20

class ATM():
    def __init__(self, cash):
        self.cash = cash

    def deposit(self):
        while True:
            if self.cash > 0:
                print("Your balance: ", self.cash)
                money = int(input("Please, enter money to deposit: "))
                self.cash += money
                print("New balance: ", self.cash)
            else:
                print("You don't have enough money")
                break

    def withdraw(self):
        while True:
            if self.cash > 0:
                print("Your balance: ", self.cash)
                money = int(input("Please, enter money to withdraw: "))
                if money <= self.cash:
                    self.cash -= money
                    print("New balance: ", self.cash)
                else:
                    print("Not enough balance.")
            else:
                print("You don't have enough money")
                break

    def check_balance(self):
        print("Your balance is", self.cash)

display = ATM(cash_now)

print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Quit
""")

while True:
    process = input("Welcome, please enter your choice: ")
    if process == 'q':
        break
    elif process == '1':
        display.deposit()
    elif process == '2':
        display.withdraw()
    elif process == '3':
        display.check_balance()
    else:
        print("Invalid choice!")

