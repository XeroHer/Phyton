#Write a program that repeatedly asks the user to input a number and calculates the sum of its digits.
#  The program should continue asking for input until the user enters 0, at which point the program should stop
total_sum=0
# Start a while loop to repeatedly ask for user input
"""while True:
     # Ask the user for a number
    user_input=input("Enter the number or(Enter 0 to stop)")
     # Check if the input is '0' to stop the loop
    if user_input=="0":
        break
     # Make sure the input is a valid number
    if user_input.isdigit():
         # Calculate the sum of digits of the entered number
        number=int(user_input)
        digit_sum=sum(int(digit) for digit in str(number))
        total_sum+=digit_sum
        print(f"The sum of digits of {number} is {digit_sum}.")
    else:
        print("Invalid Number")
print(f"The total sum of all digits is: {total_sum}")
#Write a program that asks the user for a number and then counts down from that number
#  to 1, printing each number. The countdown should stop once it reaches 1.
user=int(input("Enter the number or(Enter 0 to stop)"))
count=0
while user>0:
    print(user)
    user-=1
#Write a program that calculates the factorial of a number entered by the user. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
#  Continue asking for input until the user enters a negative number, at which point the program should end.
u=int(input("Enter the number or(Enter 0 to stop)"))
factorial=1
i=1
while i<=u:
    factorial*=i
    i+=1
print(factorial)
#Write a program that asks the user for a number and prints its multiplication table up to 10. 
# The program should continue to ask for new numbers and print the table until the user enters 0.
while True:
    number=int(input("Enter the Number::"))
    if number=="0":
        print("Program Ended")
        break
        print(f"Multiplication table for {number}:")
    for i in range(1,11):
        print(f"{number}x{i}={number*i}")
    print()"""
#Write a program that asks the user to input a string and checks if the string is a palindrome (a word that reads the same forward and backward). 
# The program should continue to ask for new strings until the user enters "exit".
while True:
    words=input("Enter the words:")
    if words.lower()=='exit':
        print("Exit")
        break
    if words==words[::-1]:
        print("words is a pallidrome")
    else:
        print("words is not a pallidrome")


#Write a program that prints out the Fibonacci sequence up to a number provided by the user. 
# The program should keep printing numbers until the number is greater than or equal to the number the user provided.

#Write a program that checks if a given number is prime or not. 
# The program should ask the user for a number and keep checking prime numbers until the user enters 0 to exit.





