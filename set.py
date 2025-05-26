#Given two sets A and B, write a function that returns their union without using the built-in union() method or the | operator.
"""def union_set(A,B):
    result=set()
    for element in A:
        result.add(element)
    for element in B:
        result.add(element)

    return result
A={1,2,3}
B={4,5,6}
print(union_set(A,B))

#Write a Python program that finds the symmetric difference of two sets (elements that are in either of the sets, but not in both).
def sysm_diff(A,B):
    result=set()
    for element in A:
        if element not in B:
            result.add(element)
    for element in B:
        if element not in A:
            result.add(element)
    return result
A={1,2,3}
B={3,5,6}
print(sysm_diff(A,B))
#Create a function that checks if one set is a subset of another set. If it is, return True; otherwise, return False.
def is_subset(A,B):
    for element in A:
        if element not in B:
            return False
    return True
A={1,0,3}
B={1,2,3,4,5,6}
print(is_subset(A,B))
#Write a Python function that takes two sets and returns the elements that are in the first set but not in the second set.
def differen(A,B):
     res=set()
     for element in A:
          if element not in B:
               res.add(element)
     return res
B={1,2,3}
A={1,2,3,4,5,6}
print(differen(A,B))
#Write a Python program that removes duplicates from a list using sets and returns the unique elements.
def remove_dupli(input_lis):
    unique_elemnt=list(set(input_lis))
    return input_lis
input_lis={1,2,3,4,3,3,4}
print(remove_dupli(input_lis))
#Write a function that checks if a given element is present in a set or not.
def is_element(element, my_set):
    if element in my_set:
        return True
    else:
        return False
my_set={1,2,3,4,5,6,7,8,9}
print(is_element(2,my_set))"""


"""#Write a Python program that takes multiple sets and returns their intersection (common elements).
Write a Python program that takes multiple sets and returns their intersection (common elements).
Set Cartesian Product:

Write a Python program to find the Cartesian product of two sets (all pairs of elements, one from each set).
Frozenset Operations:

Create a Python function that demonstrates the use of frozenset by performing set operations (union, intersection, difference).
Set Operations on List of Sets:

Write a Python function that accepts a list of sets and returns the union of all sets in the list.
Count Occurrences of Set Elements in List:

Write a Python program to count the occurrences of elements in a list and return a set of the elements that appear more than once.
Find Subset and Superset Relation:

Create a function that checks whether one set is a superset or subset of another set and prints an appropriate message.
Find Common Elements from Multiple Lists:

#Write a Python program that takes multiple sets and returns their intersection (common elements).
#Write a Python program that takes multiple sets and returns their intersection (common elements).

def coomon_set(list_of_list):
    common_list=set(list_of_list[0])

    for i in list_of_list[1:]:
        common_list &=set(i)
    
    return list(common_list)
list_of_list=[
    [1,2,3,4,5],
    [1,3,8,9,0],
    [1,3,5,7,9]
]
output=coomon_set(list_of_list)
print(output)
#Write a Python program to find the Cartesian product of two sets (all pairs of elements, one from each set).
import itertools
set1={1,2,3,4,5}
set2={'a','b','c','d','e'}
merged=list(itertools.product(set1,set2))
print("merged")
for pairs in merged:
    print(pairs)"""
#Create a Python function that demonstrates the use of frozenset by performing set operations (union, intersection, difference).
