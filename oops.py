class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    
    def menu(self):
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
        self.pin = input("Create your pin: ")
        print("PIN created successfully.")
        self.menu()
    
    def deposit(self):
        temp = input("Enter your pin:  ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("You have deposited:", amount)
            print("Your new balance is:", self.balance)
        else:
            print("Invalid pin.")
        self.menu()
    
    def withdraw(self):
        temp1 = input("Enter your pin: ")
        if temp1 == self.pin:
            amount1 = int(input("Enter amount to withdraw: "))
            if amount1 <= self.balance:
                self.balance -= amount1
                print("You have withdrawn:", amount1)
                print("Your new balance is:", self.balance)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid pin.")
        self.menu()
    
    def check_balance(self):
        temp2 = input("Enter your pin:  ")
        if temp2 == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid pin.")

        self.menu()
    

sbi = Atm()


         
