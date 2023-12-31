# This is a bank class
class BankingSystem:

    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    # This is a deposit method
    def Deposit(self,amount):
        self.balance += amount
        print(f"{self.account_number} is been deposited {amount} rupees in bank")

    # This is a withdrawal method
    def Withdrawal(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{self.account_number} has withdrawal {amount} rupees from bank")

        else:
            print("Insufficent funds!")

    # This method check the balance
    def Balace_check(self):
        print(f"Accout Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance is {self.balance}")

    # This method gives options to user
    def Atm_Options(self):
        print("(1 for deposit)")
        print("(0 for withdrawal)")
        print("(2 for balance check)")

# This function is use to set a pin in atm
def pin():
    pin = 1807
    user = int(input("Enter your pin here: "))

    if pin != user:
        raise ValueError("Your Pin Has Been Blocked")
    
    else:
        bank()

# This is the main function
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