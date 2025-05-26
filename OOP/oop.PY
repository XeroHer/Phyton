import math


class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print(sum/3)
    

s1=Student("Amit",[34,45,56])
s1.get_avg()
class Account:
   
    def __init__(self, balance, Acc_No):
        self.balance=balance
        self.Acc_No=Acc_No
    def debit(self, ammount):
        self.balance-=ammount
        print(ammount)
        print(self.get_balace())
    def credit(self, ammount):
        self.balance+=ammount
        print(ammount)
        print(self.get_balace())
    def get_balace(self):
        return self.balance
    
aac1=Account(900000,122344)
aac1.debit(2000)
aac1.credit(4000)

"""Qes1.Define a class called Car with the following attributes:
make (string)
model (string)
year (integer)
color (string)
Add a method get_description() that returns a string describing the car (e.g., "2020 Red Toyota Camry")."""

class Car:
    def __init__(self, make, year,model, color,):
        self.make=make
        self.year=year
        self.model=model
        self.color=color
    def get_description(self):
       return f"{self.make}{self.year}{self.model}{self.color}"

my_car = Car("Audi", 2020, "BT123", "Black")
print(my_car.get_description())

"""Q2.Inheritance and Method Overriding:

Create a base class Animal with methods speak() and eat().
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Woof!".
Create another derived class Cat that overrides speak() to print "Meow!"."""

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def eat(self):
        print("This Animal is eating")
class dog(Animal):
    def speak(self):
        print("woof")
class cat(Animal):
    def speak(self):
        print("meow")
Dog=dog()
Cat=cat()

Dog.speak()
Dog.eat()

Cat.eat()
Cat.speak()

"""Q3.Create a Rectangle Class
Write a class called Rectangle with the following properties:
width and height (initialize these properties through the constructor).
A method area() that returns the area of the rectangle.
A method perimeter() that returns the perimeter of the rectangle.
Instantiate the class and call the methods."""

class Rectangle:
    def __init__(self, width, hight):
        self.width=width
        self.hight=hight
    def area(self):
        return self.width*self.hight
    def perimeter(self):
        return 2*(self.width+self.hight)

Are=Rectangle(5,7)
print(Are.area())
print(Are.perimeter())

""" Create a BankAccount Class
Write a class called BankAccount with the following attributes:
account_holder_name, balance (initialize these through the constructor).
Create methods:
deposit(amount) to deposit money into the account.
withdraw(amount) to withdraw money from the account.
get_balance() to get the current balance.
Handle exceptions for invalid withdrawals (insufficient funds).
Create an instance of BankAccount and perform deposit, withdrawal, and check the balance."""

class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.account_holder_name=account_holder_name
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit${amount}.Current balance${self.balance}")
        else:
            print("deposit must be positive")
    def withdraw(self, amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"withdraw${amount}.Current balance${self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance
    def get_account_holder_name(self):
        return self.account_holder_name
    
account=BankAccount("Rupesh", 32874)
print("Account_holder",account.get_account_holder_name())

account.deposit(1234)
account.withdraw(5000)

print("final Price ",account.get_balance())

"""Q5.Write a class Person with:
name, age, address (initialize through the constructor).
A method info() that prints the name and age of the person.
Write another class Employee that inherits from Person and adds:
employee_id and department.
A method employee_info() that prints the employee ID and department.
Create an instance of Employee and display both personal and employee information."""

class Person:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address
    def info(self):
        print(f"The name of person:: {self.name }::age::{self.age}")
class Employee(Person):
    def __init__(self, name, age, address, employee_id, department):
        super().__init__(name, age, address)
        self.employee_id=employee_id
        self.department=department
    def employee_info(self):
        print(f"employee_Id::{self.employee_id} department:: {self.department}")


empy=Employee("roshan",21, "se18", 12345, "IT")
empy.info()
empy.employee_info()

"""Q6.Write a base class Shape with a method area() (which should raise an exception by default).
Create two derived classes Circle and Square, each implementing the area() method.
Circle should take radius as an argument and compute the area of the circle.
Square should take side as an argument and compute the area of the square.
Instantiate both classes and call their area() method."""

class shape:
    def area():
        raise NotImplementedError("subclass must be implement in area() method")
class circle(shape) :
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
class square(shape):
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side**2
    
s1=square(2)
print(s1.area())
s2=circle(3)
print(s2.area())

"""Q7.Create a class hierarchy for different types of vehicles. Implement the following:

Vehicle: A base class with a method move() that raises a NotImplementedError.
Car: A subclass of Vehicle that implements the move() method to print "The car is moving on the road."
Boat: A subclass of Vehicle that implements the move() method to print "The car is moving on the road."
Airplane: A subclass of Vehicle that implements the move() method to print "The airplane is flying in the sky."
Create instances of each vehicle and call their move() method."""

class vehicle:
    def move(self):
        raise NotImplementedError("subclass must be implement in move() method")
class car(vehicle):
    def move(self):
        print("The car is moving on the road")
class boat(vehicle):
    def move(self):
        print("The car is moving on the road")
class airplane(vehicle):
    def move(self):
        print("The airplane is flying in the sky")
ar=car()
Baot=boat()
Airplane=airplane()

ar.move()
Baot.move()
Airplane.move()

"""Create a class Student with the following attributes:

Name of the student.
List of marks for different subjects.
The class should have the following methods:

add_marks(marks): Adds marks to the list.
average_marks(): Calculates and returns the average of the marks.
grade(): Returns the grade based on the average marks:
A: 90 and above
B: 75 to 89
C: 50 to 74
D: Below 50
Write a program to create a student, add marks, and display their average marks and grade."""

class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def add_marks(self, marks):
        self.marks.append(marks)
    def average_marks(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)
    def grade(self):
        avg=self.average_marks()
        if avg>=90:
            return 'A'
        elif avg>=75:
            return 'B'
        elif avg>=50:
            return 'C'
        else:
            return 'D'
s1=Student("Bikesh")
s1.add_marks(49)
s1.add_marks(74)
s1.add_marks(90)
s1.add_marks(95)

print(s1.name)
print(s1.average_marks())
print(s1.grade())

"""Create a Book class with the following attributes:

Title of the book
Author of the book
ISBN number
Create a Library class with the following attributes:

List of books
The Library class should have the following methods:

add_book(book): Adds a book to the library.
remove_book(isbn): Removes a book from the library using its ISBN number.
display_books(): Displays the details of all books in the library.
Write a program to add and remove books from the library and display the available books."""

class Book:
    def __init__(self, tittle, author, ISBN,):
        self.tittle=tittle
        self.author=author
        self.ISBN=ISBN
    def __str__(self):
        return f"Tittle:{self.tittle}:Author:{ self.author}:ISBN:{self.ISBN}"
class library:
    def __init__(self):
        self.books=[]  # List to store the books
    def add_book(self, books):
        self.books.append(books)
    def remove_book(self, ISBN):
        for books in self.books:
            if books.ISBN==ISBN:
                self.books.remove(books)
                print(f"Book with ISBN ISBN has been removed")
                return
            print("Book with ISBN has not found")

    def display_books(self):
        if not self.books:
            print("No books avaailable in library")
            return
        print("Book in library")
        for books in self.books:
            print(books)
book1=Book("Amit","Bikesh", 123456)
book2=Book("Rupesh","roshan", 3435353)

libeary=library()

libeary.add_book(book1)
libeary.add_book(book2)

libeary.display_books()

libeary.remove_book(123456)
libeary.display_books()


        
        


