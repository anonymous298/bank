class BankingSystem:

    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def Deposit(self,amount):
        self.balance += amount
        print(f"{self.account_number} is been deposited {amount} rupees in bank")

    def Withdrawal(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{self.account_number} has withdrawal {amount} rupees from bank")

        else:
            print("Insufficent funds!")

    def Balace_check(self):
        print(f"Accout Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance is {self.balance}")

    def Atm_Options(self):
        print("(1 for deposit)")
        print("(0 for withdrawal)")
        print("(2 for balance check)")

def pin():
    pin = 1807
    user = int(input("Enter your pin here: "))

    if pin != user:
        raise ValueError("Your Pin Has Been Blocked")
    
    else:
        bank()

def bank():
    bank_obj = BankingSystem("123456789","Talha",1000000)
    bank_obj.Atm_Options()
    
    while True:
        
        choice = int(input("Enter your options here: "))
        if choice == 1:
            money = int(input("Enter your amount to deposit: "))
            bank_obj.Deposit(money)

        elif choice == 0:
            money = int(input("Enter your amount to withdraw: "))
            bank_obj.Withdrawal(money)

        elif choice == 2:
            bank_obj.Balace_check()

pin()