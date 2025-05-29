# Write a lambda function to add 10 to a given number

# def add_ten(x):
#     return (lambda y: y + 10)(x)

# print(add_ten(3))  # Output: 13
# print(add_ten(10))  # Output: 20

#Create a lambda function that multiplies two numbers
# def multiply(x, y):
#     return (lambda a, b: a * b)(x, y)
# print(multiply(3, 4))  # Output: 12

# Use a lambda function to check if a number is even.
# def is_even(n):
#     return (lambda x: x % 2 == 0)(n)
# print(is_even(4))  # Output: True
# print(is_even(5))  # Output: False

# Sort the list [(1, 2), (3, 1), (5, 0)] based on the second element using a lambda.
# def sort_by_second_element(lst):
#     return sorted(lst, key=lambda x: x[1])
# print(sort_by_second_element([(1, 2), (3, 1), (5, 0)]))  # Output: [(5, 0), (3, 1), (1, 2)]


# Use a lambda inside map() to square all numbers in the list [1, 2, 3, 4].
# def square_numbers(lst):
#     return list(map(lambda x: x ** 2, lst))
# print(square_numbers([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]

# Use a lambda function inside filter() to get only odd numbers from [1, 2, 3, 4, 5, 6].
# def fillter_odd_numbers(lst):
#     return list(filter(lambda x: x % 2 != 0, lst))
# print(fillter_odd_numbers([1, 2, 3, 4, 5, 6]))  # Output: [1, 3, 5]

#Sort the list of strings ["apple", "banana", "cherry", "date"] by string length using a lambda.
# def sort_by_length(lst):
#     return sorted(lst, key=lambda x: len(x))
# print(sort_by_length(["apple", "banana", "cherry", "date"]))  # Output: ['date', 'apple', 'banana', 'cherry']

# Given the list ["Python", "C", "Java", "Go"], use a lambda to sort it by the last letter.
# def sort_by_last_letter(lst):
#     return sorted(lst, key=lambda x: x[-1])
# print(sort_by_last_letter(["Python", "C", "Java", "Go"]))  # Output: ['Go', 'Java', 'C', 'Python']

#Use a lambda with reduce() to compute the product of all numbers in [1, 2, 3, 4].
# def product_of_numbers(lst):
#     from functools import reduce
#     return reduce(lambda x, y: x * y, lst)
# print(product_of_numbers([1, 2, 3, 4]))  # Output: 24

# Write a lambda that returns the maximum of three arguments (hint: use with max()).
# def max_of_three(a, b, c):
#     return (lambda x, y, z: max(x, y, z))(a, b, c)
# print(max_of_three(1, 2, 3))  # Output: 3
# print(max_of_three(10, 5, 8))  # Output: 10



#Create a lambda function that returns True if a string is a palindrome.
# def is_palindrome(s):
#   return (lambda x:x ==x[::-1])(s)
# print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

# Use a lambda to convert a list of temperatures in Celsius to Fahrenheit.
# def celsius_to_fahrenheit(lst):
#        return list(map(lambda c:(c*9/5)+32, lst))
# print(celsius_to_fahrenheit([0, 20, 37, 100]))  # Output: [32.0, 68.0, 98.6, 212.0]

# Combine map() and lambda to get the lengths of each word in ["hello", "world", "lambda"].
 
def word_lengths(lst):
    return list(map(lambda x: len(x), lst))
print(word_lengths(["hello", "world", "lambda"]))  # Output: [5, 5, 6]





# Create a simple calculator using lambda functions for addition, subtraction, multiplication, and division.
# def calculator(x, y, operation):
#     return {
#         'add': (lambda a, b: a + b)(x, y),
#         'subtract': (lambda a, b: a - b)(x, y),
#         'multiply': (lambda a, b: a * b)(x, y),
#         'divide': (lambda a, b: a / b if b != 0 else 'Division by zero')(x, y)
#     }.get(operation)
# print(calculator(10, 5, 'add'))        # Output: 15
# print(calculator(10, 5, 'subtract'))   # Output: 5  
# print(calculator(10, 5, 'multiply'))   # Output: 50
# print(calculator(10, 5, 'divide'))     # Output: 2.0
# print(calculator(10, 0, 'divide'))     # Output: Division by zero

# Use a lambda function to filter out negative numbers from a list.
def filter_negative_numbers(lst):
    return list(filter(lambda x: x >= 0, lst))  
print(filter_negative_numbers([-1, 2, -3, 4, 5]))  # Output: [2, 4, 5]

