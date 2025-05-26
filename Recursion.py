#1.Write a recursive function reverse_string(s) that takes a string s as input and returns
#  the string in reverse order without using any loops or built-in reverse methods.
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]
    
print(reverse_string("hello"))

#2.Sum of Digits Write a recursive function sum_of_digits(n) that calculates the sum of the digits of a given integer n.
def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum_of_digits(n//10)
print(sum_of_digits(123456))

#3.Write a recursive function power(base, exp) that returns the result of raising base to the power of exp (i.e., base^exp)
def power(base, exp):
    if exp==0:
        return 1
    else:
        return base*power(base, exp-1)
print(power(2,3))

#4.4. Counting Occurrences Write a recursive function count_occurrences(arr, x) that returns the number of times the element x appears in the list arr