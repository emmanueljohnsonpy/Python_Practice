# Simple Example

""" def outer(x):
    x = 10
    def inner():
        nonlocal x
        x += 5
        print(x)
    inner()
    print(x)

outer(10) """

# Counter Example

""" def counter():
    x = 0
    def increment():
        nonlocal x
        x += 1
        return x
    return increment

count = counter()
print(count())
print(count())
print(count()) """

# Accumulator Example

""" def accum():
    x = 0
    def add(n):
        nonlocal x
        x += n
        return x
    return add

add = accum()
print(add(5))
print(add(10)) """

# Name meaningful variable names and function names


