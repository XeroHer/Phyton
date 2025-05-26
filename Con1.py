# 1Write a program that takes a number from the user and prints whether it is positive, negative, or zero.

number=int(input("Enter the Random Number:"))
if number==0:
    print("You Entered Zero")
elif number>0:
     print("You Entered Positive Number")
else:   
    print("You Entered Negative Number")

    #Write a Python program to check if a number entered by the user is even or odd.
num=int(input("Enter the Random Number:"))
if num==0:
    print("You Entered Zero")
elif num%2==0:
     print("You Entered Even Number")
else:   
    print("You enetered Negative Number") 

    #Take three numbers as input and print the largest one.

num1=int(input("Enter the  Number1:"))
num2=int(input("Enter the  Number2:"))
num3=int(input("Enter the  Number3:"))
    
if num1>num2 & num1>num3:
    print("Num1 is Greater than 2 and 3")
elif num2>num3 &num2>num1:
    print("Num2 is grater than 1 and 3")
else:
    print("Num3 I graeter") 

    #Write a Python program to check if a year is a leap year. 
    # A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
year=int(input("Enter the  year:"))
if (year%4==0 & year%100!=0) or(year%400)==0:
    print("Year is a leap year")
else:
    print("Not")

