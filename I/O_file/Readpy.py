# create new 

# with open("demo.txt", "x") as f:
#     f.write("Hello, Welcome the new Science")
# with open("demo.txt") as f:
#     print(f.read())

# append content to the existing file
# with open("demo.txt", "a") as f:
#     f.write("Hello, Welcome the python")
# with open("demo.txt") as f:
#     print(f.read())

# overwrite
# with open("demo.txt", "w") as f:
#     f.write("Hello,welcome to the device")
# with open("demo.txt") as f:
#     print(f.read())

# loops on to read file
with open("demo.txt") as f:
    for x in f:
        print(x)