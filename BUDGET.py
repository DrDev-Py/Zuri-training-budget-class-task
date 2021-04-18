class Budget:
    
    """This is a class that instantiates a budget
       Being able to deposit into a particular budget category, 
       withdraw from it and transfer to another budget category.
    """
    
    def  __init__(self, category):
        self.category = category
        self.balance = 0 

    def deposit(self, amount):

        """deposits into a budget
        Args:
            "amount":
            type = int: adds the amount to the present balance
        """

        self.balance += amount
        
    def withdrawal(self, amount):

        """withdraws from a budget
        Args:
            "amount":
            type = int: removes the amount to the present balance
                        returns an error if there are insufficient funds
        """

        if self.balance >= amount:
            self.balance -= amount 
        else: 
            print("insufficient funds \n withdrawal unsuccesful")

    def final_balance(self):

        """returns the balance of the current category
        """

        print(self.balance)

    def transfer(self, second, amount):

        """withdraws from the current budget,
           and transfers the same amount to a second budget
        Args:
            
            1. "second":
            type = class: this is the second budget where the amount is deposited to.
            2. "amount":
            type = int: removes the amount to the present balance
                        returns an error if there are insufficient funds
        """
        
        if self.balance < amount:
            print("Insufficient funds in donor category")
        else:
            self.balance -= amount
            second.balance += amount
        print("this is the recipient category balance ", second.balance)
        print("this is donor category balance ", self.balance)




######  ATTENTION  *** Remove the docstring below to test the code ***  ######
"""
food = Budget("food")
clothing = Budget("clothing")

food.deposit(5000)
clothing.deposit(1500)

clothing.withdrawal(500)

food.final_balance()
clothing.final_balance()

food.transfer(clothing, 10000)
food.transfer(clothing, 1000)

"""    
