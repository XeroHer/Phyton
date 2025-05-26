#Class and Objects Basics
#Question: Create a class Car with the following attributes: make, model, year, and color. Add a method display_details()
#  that prints the details of the car. Create an instance of the Car class and call the method to display its details.

class Car():
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        return f"{self.make} {self.model} {self.year} {self.color}"
     
myCar = Car("Audi", "1234BC", 2020, "red")
print(myCar.display_details())

#2.Question: Create a base class Animal with methods speak() and eat(). Then, create a subclass Dog that inherits 
# from Animal and overrides the speak() method to print "Bark!". Create an instance of Dog and call both the speak()
#  and eat() methods.
class Animal():
    def speak(self):
        print("Speak")
    def eat(self):
        print("This Animal is eating")
class Dog(Animal):
    def speak(self):
        print("Bark")
dog=Dog()
dog.speak()
dog.eat()

# Encapsulation
# Question: Define a class BankAccount with the attributes account_balance and account_holder_name.
#  Add methods to deposit and withdraw money. Make sure that the balance cannot go below zero, and provide a way to
#  get the balance through a getter method while keeping the balance attribute private.
class BankAccount():
    def __init__(self,account_balance,account_holder_name):
        self.account_balance=account_balance
        self.account_holder_name=account_holder_name
    def deposit(self, amount):
        if amount>0:
            self.account_balance+=amount
            print(f"deposit{ amount} Current Balance{ self.account_balance}")
        else:
            print("Amount must be positive ")
    def withdraw(self, amount):
            if amount>0 and amount<=self.account_balance:
                self.account_balance-=amount
                print(f"withdraw{ amount} Current Balance{ self.account_balance}")
            else:
                print("Insufficient balance")
            else:
            print("Amount must be positive ")
    
            

            

     