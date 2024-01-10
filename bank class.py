class Bank:
    def __init__(self, name, number, balance):
        self.name = name
        self.number=number
        self.balance = balance
    
    def check_account(self, number):
        if number != self.number:
            print("Account number not found")
            return False
        return True

    def deposit(self,number):
        print("Enter account number:",number)
        if self.check_account(number):
            print("Enter amount to deposit:")
            amount=float(input())
            self.balance += amount
            print("Amount deposited successfully")
        
    def withdraw(self, number):
        if self.check_account(number):
            print("Enter amount to withdraw:")
            amount=float(input())
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print("Amount withdrawn successfully")

    def display(self,number):
        if self.check_account(number):
            print("Account Deails:")
            print("Account Number:",self.number)
            print("Current Balance:",self.balance)

bank_acc=Bank("Neha",123456789,1000)
#deposit money
bank_acc.deposit(123456789)
#withdraw money
bank_acc.withdraw(123456789)
#display balance
bank_acc.display(123456789)

        


        