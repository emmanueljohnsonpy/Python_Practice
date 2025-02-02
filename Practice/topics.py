""" a=[i**2 for i in range(1,11) if i%2==0]
print(a) """


""" def my_generator():
    for i in range(10):
        yield i
    
a=my_generator()
print(next(a))
print(next(a)) """


""" def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() """


""" my_list = [1, 2, 3, 2, 4, 5, 1]
seen=set()
duplic=set()
for x in my_list:
    if x in seen:
        duplic.add(x)
    else:
        seen.add(x)

print(duplic) """


""" a=[1,2,3,4,5]
res=[x*2 if x%2==0 else x**3 for x in a]
print(res) """


""" my_string="Hello World"
res={}
for x in my_string:
    if x in res:
        res[x]+=1
    else:
        res[x]=1
print(res) """


""" import random
otp=random.randint(100000, 999999)
print(otp) """


""" def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, a=3, b=4) """


""" add = lambda a, b : a+b
square = lambda a: a**2
even = lambda a: a%2==0
print(add(2,5))
print(square(5))
print(even(8)) """


""" class Myclass():
    def __init__(self, value):
        self.value=value

obj=Myclass(5)
print(obj.value) """


""" import sys
x = "yooo"
print(sys.getsizeof(x))  # Size of integer object """


x = 2
assert x > 5, "x should be greater than 5"
