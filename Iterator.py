# # Create a class MyRange that mimics the built-in range() function using iterators
# class myRange:
#    def __init__(self, start, stop=None, step=1):
#         if stop is None:
#            self.start=0
#            self.stop=start
#         else:
#            self.start=start
#            self.stop=stop
        
#         if step==0:
#               raise ValueError("step must not be zero")
#         self.step = step
#         self.current = self.start

#    def __iter__(self):
#        self.current = self.start
#        return self
#    def __next__(self):
#        if(self.step>0 and self.current>=self.stop) or (self.step<0 and self.current<=self.stop):
#            raise StopIteration
       
#        current_value = self.current
#        self.current += self.step
#        return current_value
       
       
# # Example usage of myRange
# for i in myRange(2,20, 2):
#     print(i)

#Create a class Countdown that takes a number n and iterates down to 0.
# class Countdown:
#     def __init__(self, n):
#         self.n=n
#         self.current=n

#     def __iter__(self):
#         self.current=self.n
#         return self
    
#     def __next__(self):
#         if self.current<0:
#             raise StopIteration
#         value=self.current
#         self.current -= 1
#         return value

# for i in Countdown(5):
#   print(i)

#Create an iterator that yields only even numbers from a list.
# class EvenIterator:
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.index = 0
    
#     def __iter__(self):
#        return self
    
#     def __next__(self):
#         while self.index<len(self.numbes):
#             value = self.numbers[self.index]
#             self.index += 1
#             if value % 2 == 0:
#                 return value
#         raise StopIteration

# # Example usage of EvenIterator
# even_numbers = EvenIterator([1, 2, 3, 4, 5, 6]) 
# for num in even_numbers:
#     print(num)  # Output: 2, 4, 6

# Write a class ReverseIterator that takes a list and iterates through it in reverse order.
class ReverseIterator:
    def __init__(self,list):
        self.list=list
        self.index=len(list)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<0:\
            raise StopIteration
        value = self.list[self.index]
        self.index -= 1
        return value
# Example usage of ReverseIterator  
reverse_iter = ReverseIterator([1, 2, 3, 4, 5])
for item in reverse_iter:
    print(item)  # Output: 5, 4, 3, 2, 1





# Question
# Create a custom iterator PeekableIterator that allows peeking the next value without advancing the iterator.

# Methods: next(), peek()

# Cycle Iterator

# Implement an iterator CycleList that cycles through elements of a list infinitely (stop after n iterations to avoid infinite loop during testing).

# 🔴 Advanced Level
# Prime Number Iterator

# Write an infinite iterator that yields prime numbers.

# Use __iter__ and __next__.

# Fibonacci Sequence Iterator

# Create an iterator that returns the Fibonacci sequence up to n elements.

# Chained Iterators

# Implement a class that takes multiple iterators and iterates through them one after the other.

# Example: Chained([iter1, iter2, iter3])

# Flatten Nested List Iterator

# Given a nested list like [1, [2, 3], [4, [5, 6]], 7], write an iterator to yield elements in a flattened manner.
    

