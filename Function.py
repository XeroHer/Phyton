#Write a function greet(name) that takes a name as an argument and prints "Hello, <name>!".

def greet(name):
    print(f"Hello, {name}!")
greet("Antima")

#Write a function greet(name) that takes a name as an argument and prints "Hello, <name>!".
def sum(a,b):
   print(a+b)
sum(2,4)
#Write a function is_even(n) that takes an integer and returns True if it's even, otherwise False.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

print(is_even(3))
#Write a function factorial(n) that returns the factorial of n using recursion.
def factorial(n):
    if n==0 or n==1:# base case
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
#Write a function find_max(lst) that takes a list of numbers and returns the maximum value.
def Max_val(lst):
    if not lst:
        return None
    
    max_num=lst[0]
    for num in lst:
        if num>max_num:
            max_num=num

    return max_num
print(Max_val([1,2,3,4,5,6,7,8]))





# Prime Number Checker:
# Write a function is_prime(n) that checks if a given number is prime.

# Lambda Function for Square:
# Write a lambda function to find the square of a number.

# Higher-Order Function:
# Write a function apply_function(func, value) that takes a function and a value, then applies the function to the value.

#Write a function is_palindrome(s) that checks if a given string is a palindrome.
def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase for uniformity
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))


# Advanced Function Questions
# Fibonacci Sequence:
# Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.
def fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))
    