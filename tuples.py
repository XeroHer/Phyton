#1.Create a tuple with the elements 10, 20, 30, 40, 50. What is the output if you print tuple[2]?
tup=[10, 20, 30, 40, 50]
print(tup[2])

#2.Write a Python program to find the length of a tuple that contains five strings.
top=[10, 20, 30, 40, 50]
print(len(top))

#Given two tuples tuple1 = (1, 2, 3) and tuple2 = (4, 5), write a Python program to concatenate these tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tupel3=tuple1+tuple2
print(tupel3)

#Create a tuple with the following structure: (1, (2, 3), 4). Access the second element inside the nested tuple.
tup2=(1, (2, 3), 4)
prin=tup2[1][1]
print(prin)

#Given a tuple t = (3, 4, 5), write a Python program to repeat the tuple twice.
t = (3, 4, 5)
print(t*2)

#Check if the number 50 is present in the tuple t = (10, 20, 30, 40)
t1 = (10, 20, 30, 40)
print(50 in t)

#Convert the tuple t = (10, 20, 30) into a list and add the element 40 to the list. After adding the element, convert it back to a tuple and print it.
t = (10, 20, 30)
l=list(t)
l.append(11)
print(l)
t2=tuple(l)
print(t2)
print(max(t2))
print(min(t2))


x = (10, 20, 30)
y, z, w = x
print(z)
