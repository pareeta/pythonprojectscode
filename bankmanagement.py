class BMS:
    def __init__(self,name):
        self.bankname=name
        self.customers=[]

    def add_customer(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        code = input("Enter a unique code: ")
        balance = float(input("Enter the starting balance: "))
        self.customers.append(
            {
                "name":name,
                "email":email,
                "code":code,
                "balance":balance,
                "transactions":[]
            }
        )
        print(f"Customer added: {name}")

    def add_money(self):
        code = input("Enter your code: ")
        amount = float(input("Enter the amount you want to add: "))
        for customer in self.customers:
            if customer["code"]==code:
                customer["balance"] += amount
                customer['transactions'].append({
                    "amount":amount,
                    "Type":"IN"
                }
                )
                print(f"Transaction successful..  your new balance is {customer['balance']}")
                break
            else:
                print("Invalid code")

    def withdraw_money(self):
        code = input("Enter your code: ")
        amount = float(input("Enter the amount you want to withdraw: "))
        for customer in self.customers:
            if customer["code"]==code:
                if customer["balance"]>= amount:
                    customer["balance"]-=amount
                    customer["transactions"].append({
                        "amount":amount,
                        "Type":"out"
                    })
                    print(f"Amount withdrawn successfully. New balance: {customer['balance']}")

                else:
                    print("insufficient balance")
                break
        else:
            print("invalid code")

    def show_transactionhistory(self):
        code = input("Enter your code to see your transaction history: ")
        for customer in self.customers:
            if customer["code"]==code:
                for transaction in customer["transactions"]:
                    print(f"Amount: {transaction['amount']}, 'Type': {transaction['Type']}")
                    break
        else:
            print("invalid code")
bank = BMS("AXIS bank")

if __name__ == "__main__":
    while True:

        print('''
            1. Add Customer
            2. Add Money
            3. Withdraw Money
            4. Show Transaction History
            ''')
        choice = input("Enter your choice: ")
        if choice == "1":
            bank.add_customer()
        if choice == "2":
            bank.add_money()
        if choice == "3":
            bank.withdraw_money()
        if choice == "4":
            bank.show_transactionhistory()

        option = input("Press c to continue and any other key to exit: ")
        if option != "c":
            break















