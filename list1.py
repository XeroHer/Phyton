#1.Create a list of 5 numbers. Add a new element at the end of the list. Remove the second element of the list. Print the final list.
list=[1,2,3,4,5]
print(list)
list.append("6")# add one elements at the end
print(list)
list.remove(2)# remove the elements
print(list)

#2.Given a list of 10 numbers, print the first 3 elements, the last 3 elements, and every second element.
pist=[1,2,3,4,5,6,7,8,9,8]
print(pist)
print(pist[:3])# print first three element
print(pist[-3:])#print last  three element
print(pist[::2])

#3.Write a list comprehension that generates a list of the squares of the numbers from 1 to 10.
squares=[x**2 for x in range(1, 11)]
print(squares)

 #4. Create a list of even numbers from 1 to 10:
even=[x for x in range(1, 10) if x%2==0]
print(even)

#5.Convert all strings in a list to uppercase:
name=["names", "apples", "ambika", "antima"]
upper_case=[name.upper() for name in name]
print(upper_case)

#6.Given a list of numbers, count how many times a specific number (e.g., 5) appears in the list.
arr=[1,2,3,4,5,4,3,5,5,4,3,4,5.5,5]
print(arr.count(5))

#.7 Create a list of random numbers and sort them in ascending order. After sorting, print both the original and sorted list.
random=[1,3,5,4,1,6,9,8];
cop=random.copy()
random.sort()
print(cop)
print(random)

#8. Create a list that contains other lists. For example, [[1, 2], [3, 4], [5, 6]]. Access the second element of the second list.
arry=[[1, 2], [3, 4], [5, 6]]
print(arry[0][1])

#9Find the length of a list and calculate the average of the numbers in the list.
andom=[1,3,5,4,1,6,9,8]
print(len(andom))
print(sum(andom)/2)

#10.Create a list of strings and sort them alphabetically.
mame=["n","am","e","s"]
mame.sort()
print(mame)

#11.Given a list of numbers, find the maximum and minimum value in the list.
andom=[1,3,5,4,1,6,9,8]
print(max(andom))
print(min(andom))

#Create a list of 10 integers and print the first, last, and middle element.
marks=[1,2,3,4,5,6,7,8,9,9,]
print((marks[0]))
print((marks[-1]))
print(marks[len(marks)//2])