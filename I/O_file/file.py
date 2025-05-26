#Write a Python program that reads a text file and counts the number of words in it. Display the total word count
"""count=0
with open("D:\Phyton\I\O_file\sample.txt", "r") as f:
    data=f.read()
    print(data)
for i in data:
    print(i)
    count+=1
#2.Write a Python program that reads a text file and counts the number of words in it.
#  The program should handle any file path input and print the total number of words.
count=0
with open("D:\Phyton\I\O_file\sample.txt","r") as f:
    data=f.read()
    print(len(data))

for i in data:
    print(i)
    count+=1
from importlib.resources import contents


def word_count(file_input):
    try:
        # Open the file using the file path provided by the user
        with open(file_input, "r") as f:
            content = f.read()

        # Split the content into words and count them
        words = content.split()
        words_C = len(words)
        print(f"Total number of words: {words_C}")
#PROBLEM
    
    except FileNotFoundError:
        print(f"The file at {file_input} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input file path from the user
file_input = input(r"D:\Phyton\I\O_file\sample.txt ")

# Call the function to count words
word_count(file_input)"""

#2Write a Python program that reads the contents of one file and writes it into another file.
#  Ensure that the destination file is overwritten, and handle the case where the source file does not exist.
def file_content(source_file, Destination_file):
    try:
        with open("source_file","r") as srx:
            data=srx.read()
        with open("source_file","w") as sr:
            dest=sr.write()
            print(f"Content from '{source_file}' has been successfully copied to '{Destination_file}'.")
    except FileNotFoundError:
        print(f"The source file '{source_file}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
source_file = input(r"D:\Phyton\I\O_file\sample.txt ")
Destination_file = input(r"D:\Phyton\I\O_file\dsti.txt ")
file_content(source_file, Destination_file)

