class Budget:

    # nameOfCustomer = input("What is your name? \n")

    def __init__(self, name,):
        self.name = name
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def deposit(self):
        amount = int(input("How much do you want to deposit? \n"))
        category = int(input("Where do you want to deposit your money? \n 1 - food \n 2 - clothing \n 3 - entertainment \n"))

        if category == 1:
            self.food += amount
            # print(self.food)
        elif category == 2:
            self.clothing += amount
            # print(self.clothing)
        elif category == 3:
            self.entertainment += amount
            # print(self.entertainment)
        else: 
            print("You selected an invalid option")

            Budget.deposit(self)

    def withdraw(self):
        amount = int(input("How much do you want to deposit? \n"))
        category = int(input("Where do you want to withdraw your money from? \n 1 - food \n 2 - clothing \n 3 - entertainment \n"))

        if category == 1:
            self.food -= amount
            # print(self.food)
        elif category == 2:
            self.clothing -= amount
            # print(self.clothing)
        elif category == 3:
            self.entertainment -= amount
            # print(self.entertainment)
        else: 
            print("You selected an invalid option")

            Budget.withdraw(self)

    def balance(self):
        checkBalance = int(input("What category balance do you want to check? \n 1 - food \n 2 - clothing \n 3 - entertainment \n"))

        if checkBalance == 1:
            return self.food
        elif checkBalance == 2:
            return self.clothing
        elif checkBalance == 3:
            return self.entertainment
        else: 
            print("You selected an invalid option")
            Budget.balance(self)   

newBudget = Budget('Emmanuel')
newBudget.deposit()