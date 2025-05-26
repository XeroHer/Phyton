#### WHILE LOOPS ####
#1.Write a program that continuously asks the user to input numbers 
# and adds them to a running total. The program should stop when the total exceeds 100.
total=0
while total<=100:
    number=int(input("Enter the Number::"))
    total+=number
    print(total)
#2.Print numbers 1 to 10: Write a Python program using a while loop to print all numbers from 1 to 10.
count=0;
while count<=100:
    print(count)
    count+=1
#3.Sum of numbers: Write a Python program that calculates the sum of all integers from 1 to a given number n using a while loop
n=int(input("Enter The Number:"))
total=0
i=1
while i<=n:
    total+=i
    i+=1
print(total)
#Write a Python program using a while loop to compute the factorial of a given positive integer.
n=int(input("Enter The Number:"))
factorial=1
if n<1:
    print("please enter positive number")
else:
    i=1
    while i<=n:
        factorial*=i
        i+=1

print(factorial)
#Create a number guessing game using a while loop where the program randomly selects a number between 1 and 100,
#  and the user has to guess it. The program should give hints if the guess is too high or too low.
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Start the guessing game
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

while True:
    # Ask the user for a guess
    guess = int(input("Enter your guess: "))
    
    # Increment the number of attempts
    attempts += 1
    
    # Check if the guess is correct
    if guess < secret_number:
        print("Your guess is too low. Try again!")
    elif guess > secret_number:
        print("Your guess is too high. Try again!")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
#Write a program that asks the user for a number and prints its multiplication table up to 10. 
# The program should continue to ask for new numbers and print the table until the user enters 0.