""" numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)

coords = (4, 5, 6)
x, y, z = coords
print(x, y, z) """


""" values = [1, 2, 3, 4, 5]
a, *b, c = values
print(a, b, c) """


""" word = "Hi"
a, b = word
print(a, b) """


""" s = {1, 2, 3, 4, 5, 6}
a, b, c, d, e, f = s
print(a, b, c, d, e, f) """


""" person = {"name": "John", "age": 30}
a, b = person
print(a, b)

a, b = person.values()
print(a, b)

a, b = person.items()
print(a, b) """


""" items = ["a", "b", "c"]
for index, value in enumerate(items):
    print(index, value)

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for k, v in zip(list1, list2):
    print(k, v) """


""" def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(func(*args))

kwargs = {"a": 1, "b": 2, "c": 3}
print(func(**kwargs)) """


# Unpacking a Tuple or List

""" values = (10, 20, 30)
a, b, c = values
print(a, b, c)

numbers = [1, 2, 3]
x, y, z = numbers
print(x, y, z) """


# Using * for Extended Unpacking

""" numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a, b, c) """


# Unpacking in a Function

""" def add(x, y, z):
    return x + y + z

values = (10, 20, 30) # Unpacking tuple into function arguments
print(add(*values)) """


# Unpacking a Dictionary

""" person = {"name": "Ronaldo", "age": 40}

# Unpacking keys
a, b = person
print(a, b)

# Unpacking values
a, b = person.values()
print(a, b)

# Unpacking into function parameters
def asking(name, age):
    return f"Yo {name} are you {age} years old ?"

print(asking(**person)) """
