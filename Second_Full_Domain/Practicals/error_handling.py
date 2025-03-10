

# variadic function that throws error if a kwarg of name 'err' is present

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    if "err" in kwargs:
        raise ValueError("Don't use err as key")
    print("No error raised")

try:
    my_func(10, 20, 30, a = "yo", err = "This will trigger error")
except ValueError as e:
    print(e)


# throwing error

def my_func(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Dont enter zero as num2")
    return num1 / num2

try:
    print(my_func(10, 0))
except ZeroDivisionError as e:
    print(e)


# error handling (except)

""" try:
    res = 3 + "3"
except Exception as e:
    print(e) """

def my_func(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Don't enter 0 as number 2 bro")  
    print("result", n1 / n2)  

try:
    n1 = int(input("enter number 1: "))
    n2 = int(input("enter number 2: "))
    my_func(n1, n2)
except ZeroDivisionError as e:
    print(e)
else:
    print("Yo bro no exceptions occured")
finally:
    print("Everything completed")