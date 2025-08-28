class Atm:
    def __init__(self):

        # instance variables for  which values of variables are different for different objects
        self.__pin = ''  # private variable(__pin)
        self.__balance = 0 # private variable(__balance)
        self.__menu()
    
    def get_pin(self):
        return self.__pin
    
    def get_balance(self):
        return self.__balance
    
    def set_pin(self,new_pin):
        if type(new_pin) == str and len(new_pin) == 4 and new_pin.isdigit():
           self.__pin = new_pin
        print("PIN updated successfully.") 


    
    def __menu(self):
        while True:
            user_input = input("""
                     Hello, how would you like to proceed?
                           1. create pin
                           2. deposit
                           3. withdraw
                           4. check balance
                           5. exit

Enter your choice: """)
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()    
            elif user_input == '5':
                print("Thank you for using SBI ATM. Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
    
    def create_pin(self):
        self.__pin = input("Create your pin: ")
        print("PIN created successfully.")
    
    def deposit(self):
        temp = input("Enter your pin:  ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__balance += amount
            print("You have deposited:", amount)
            print("Your new balance is:", self.__balance)
        else:
            print("Invalid pin.")
    
    def withdraw(self):
        temp1 = input("Enter your pin: ")
        if temp1 == self.__pin:
            amount1 = int(input("Enter amount to withdraw: "))
            if amount1 <= self.__balance:
                self.__balance -= amount1
                print("You have withdrawn:", amount1)
                print("Your new balance is:", self.__balance)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid pin.")
    
    def check_balance(self):
        temp2 = input("Enter your pin:  ")
        if temp2 == self.__pin:
            print("Your balance is:", self.__balance)
        else:
            print("Invalid pin.")
    
    
sbi= Atm()
# print(sbi.__pin)  # This will raise an AttributeError since __pin is a private variable
# print(sbi.__balance)  # This will raise an AttributeError since __balance is a private variable
# print(sbi.__menu())  # This will raise an AttributeError since __menu is a private method

sbi.set_pin("4321")
sbi.get_pin()
sbi = Atm()
print(sbi.get_pin())