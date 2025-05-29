
# You are given the following code snippet:

# python
# Copy
# Edit
x = 5
def outer():
    x = 10
    def inner():
        x = 15
        print("Inner x:", x)
    inner()
    print("Outer x:", x)
outer()
print("Global x:", x)
# 🔧 Your Task:
# Predict and explain what the output will be.
# Modify the inner() function so that it modifies the x defined in outer(), not the local one in inner() (use nonlocal).
# Modify the inner() function so that it modifies the global x instead (use global).
# After each modification, print the values of x at all three levels (inside inner, inside outer, and globally)

x = 5
def outer():
    x = 10
    def inner():
        nonlocal x 
        x= 15
        print("Inner x:", x)
    inner()
    print("Outer x:", x)
outer()
print("Global x:", x)


x = 5
def outer():
    x = 10
    def inner():
        global x 
        x= 15
        print("Inner x:", x)
    inner()
    print("Outer x:", x)
outer()
print("Global x:", x)