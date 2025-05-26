for el in range(10):
    pass
print(el)
#Basic Class Placeholder:
#Create an empty class Person using the pass statement.
class person:
    pass
#Write a for loop that iterates from 1 to 10 but does nothing inside the loop using pass.
for bl in range(1,10):
    pass
#Write a function that checks if a number is positive, negative, or zero.
#  Use pass inside the negative and zero conditions but print a message for positive numbers.
def check_num(num):
    if num>0:
        print("You Enter the Positive Number")
    if num<0:
        pass
    else:
        pass
check_num(3)
check_num(-2)
check_num(0)

#Write a try-except block where the except clause catches a ZeroDivisionError but does nothing using pass.
try:
    result=10/0
except ZeroDivisionError:
    pass

print("Program continous running.....")
#Abstract Method Placeholder:
#Create a class Animal with a method make_sound(), but don't implement it—just use pass. Then, create a subclass 
# Dog that overrides make_sound() to print "Bark!".
class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("bark!")

dog=Dog()
dog.make_sound()