#1.Write a Python program to count the occurrences of each character in a string using a dictionary.
def count_char_occurence(input_str):
 # Initialize an empty dictionary to store character counts
    char_count={}
     # Loop through each character in the string
    for char in input_str:
        if char in char_count:
             # If the character is already in the dictionary, increment its count
            char_count[char]+=1
        else:
             # Otherwise, add the character to the dictionary with a count of 1
            char_count[char]=1

    return char_count
    
input_str="abcdef"
outup=count_char_occurence(input_str)
print(outup)

#2.Write a Python function that merges two dictionaries. 
# If the same key exists in both, the value from the second dictionary should override the first dictionary’s value.
def merged_Dic(dic1, dic2):
     # Use the update() method to merge dict2 into dict1
    dic1.update(dic2)
    return dic1

dic1={'a':1,'b':2}
dic2={'b':2, 'c':3}
dic3=merged_Dic(dic1, dic2)
print(dic3)

#3.Write a Python program that finds the key with the maximum value in a dictionary
def max_value(input_Div):
     # Find the key with the maximum value using the max function
    max_num=max(input_Div ,key=input_Div.get)
    return max_num
print(max_value({'a': 1, 'b': 2, 'c': 3}))

#4.Write a function to invert a dictionary, swapping keys and values.
def swapp(input):
     # Use dictionary comprehension to swap keys and values
     swapping={value: key for key, value in input.items()}
     return swapping

print(swapp({'a': 1, 'b': 2, 'c': 3}))

#Write a function that takes two dictionaries and merges them. 
# If there is a common key, the value in the second dictionary should overwrite the value in the first one.
def meged_Dic(dic1, dic2):
     dic1.update(dic2)
     return dic1

dic1={'a':1,'b':2}
dic2={'b':2, 'c':3}
dic3=meged_Dic(dic1, dic2)
print(dic3)

  # Write a function that takes a string as input and returns
  #  a dictionary where the keys are characters and the values are the number of times each character appears in the string
def char_occurence(input_str):
     char_count={}
     for char in input_str:
          if char in char_count:
               char_count[char]+=1
          else:
               char_count[char]=1
     return char_count

print(char_occurence("abcdef"))

#Write a function that inverts a dictionary. The keys become values, and the values become keys. 
# If there are duplicate values in the original dictionary, the inverted dictionary should store them in a list.
def inverted_dic(original_dic):
     inved_dic={}
     for key, value in original_dic.items():
          if value not in inved_dic:
               inved_dic[value]=[key]
          else:
               inved_dic[value].append(key)
     return inved_dic

original_dic={'a': 1, 'b': 2, 'c': 2, 'd': 3}
output=inverted_dic(original_dic)
print(output)

#Write a Python function that checks if a given key exists in a dictionary, 
# and returns a message indicating whether the key is present or not.
def check_dic(my_dic, key):
     if key in my_dic:
          return "key exists in the dictionary"
     else:
          return "key doesn't exist in the dictionary"

my_dic={'name':'amit','age':'21','country':'neapl'}
key='age'
print(check_dic(my_dic, key))

#Write a Python function that removes all keys from a dictionary where the value is a specified number.
def remove_key_by_value(d, value_to_remove):
     return {key: value for key, value in d.items() if value!=value_to_remove}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
new_dic= remove_key_by_value(my_dict, 1)
print(new_dic)

#Write a function common_keys(dict1, dict2) that returns the common keys between two dictionaries
def common_key(dict1, dict2):
     return list(dict1.keys() & dict2.keys())

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(common_key(dict1, dict2))

#Write a function that removes a specific key from a dictionary. If the key doesn't exist, return a message saying "Key not found."

def remove_key(dict, key):
     if key in dict:
          del dict[key]
     return dict
dict={'a': 1, 'b': 2, 'c': 3}
print(remove_key(dict,'b'))

#Given a dictionary, write a Python function to sort the dictionary by its values in ascending or descending order
def sorted_disc_by_value(dictionary, order='asec'):
     sorted_dic=dict(sorted(dictionary.items(), key=lambda item:item[1], reverse=(order=='desc')))
     return sorted_dic
my_dict = {'a': 3, 'b': 1, 'c': 2}
print(sorted_disc_by_value(my_dict, 'asec'))
print(sorted_disc_by_value(my_dict, 'desc'))