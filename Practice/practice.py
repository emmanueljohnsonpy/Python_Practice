# closure

def outer_function(mess):
    def inner_function():
        print(mess)
    return inner_function

temp=outer_function("hai how are you")
temp()

# unpacking

""" fruits=('apple', 'banana', 'cherry')        #Basic Unpacking
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3) """

""" sport_list = ['tony', 'soccer', 'basketball', 'baseball', 90, 80, 90]       #Advanced Unpacking with *
name, *games, score1, score2, score3 = sport_list
print(name, games, score1, score2, score3) """

""" def myfunc(a, b, c, d):         #Unpacking in Function Calls
    print(a, b, c, d)

mylist=[1,2,3,4]
myfunc(*mylist) """

""" def myfunc(a, b, c):        #Unpacking Dictionary Items
    print(a, b, c)

d={'a': 2, 'b': 4, 'c': 10}
myfunc(**d) """

#Logical AND

""" a = 1 and False and 5       
print(a) """

#decorator to prepend string

""" def prepend_string(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}"
        return wrapper
    return decorator

# Example usage
@prepend_string("Prefix: ")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice")) """

#remove key corresponding to the highest value in dict

""" my_dict = {'A': 100, 'B': 10, 'C':50, 'D':5}
hightest = 0
corresponding_key = ""
for x,y in my_dict.items():
    if hightest < y:
        hightest = y
        corresponding_key = x
del my_dict[corresponding_key]
print(my_dict) """

#removing an object key

""" my_dict = {'A': 100, 'B': 10, 'C':50, 'D':5}
# del my_dict['A']              #1
# r=my_dict.pop('A')            #2
# print(r)
# k, v = my_dict.popitem()      #3
# print(k, v)
print(my_dict)
"""











































