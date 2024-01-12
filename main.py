# This is a bank class
class BankingSystem:

    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    # This is a deposit method
    def Deposit(self,amount):
        self.balance += amount
        print(f"\n{self.account_number} is been deposited {amount} rupees in bank")

    # This is a withdrawal method
    def Withdrawal(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"\n{self.account_number} has withdrawal {amount} rupees from bank")

        else:
            print("Insufficent funds!")

    # This method check the balance
    def Balace_check(self):
        print(f"\nAccout Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Current Balance is {self.balance}")

    # This method gives options to user
    def Atm_Options(self):
        print("\n(1 for deposit)")
        print("(2 for withdrawal)")
        print("(3 for balance check)")
        print("(0 to quit)")

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

        choice = int(input("\nEnter your options here: "))
        if choice == 1:
            money = int(input("\nEnter your amount to deposit: "))
            bank_obj.Deposit(money)

        elif choice == 2:
            money = int(input("\nEnter your amount to withdraw: "))
            bank_obj.Withdrawal(money)

        elif choice == 3:
            bank_obj.Balace_check()

        elif choice == 0:
            break
          
        else:
            print("Invalid Input!")

    choice = input("\nDo you want to continue(y/n): ").lower()

    if choice != "y":
      print("OK No Problem")

    else:
      bank()
      
if __name__ == "__main__":
    pin()