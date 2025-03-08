

# Simple example

def outer_func(name):
    def inner_func():
        print(f"Hai, {name}")
    return inner_func

res = outer_func("Emmanuel")
res()


# Another example

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_instance = outer_function(10)
print(closure_instance(5))
print(closure_instance(20))


# Maintaining State with Closures

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = counter()
print(c1())
print(c1())

c2 = counter()
print(c2())
print(c2())


# Encapsulation Using Closures

def bank_account(initial_balance):
    balance = initial_balance   # balance is hidden from direct access.
    def transaction(amount):    # The transaction() function provides controlled access to modify balance.
        nonlocal balance
        balance += amount
        return balance
    return transaction

add = bank_account(100)
print(add(20))
print(add(-30))


# Function Factory with Closures

def multiplier(factor):
    def multiply_by(num):
        return num * factor
    return multiply_by

double = multiplier(2)
triple = multiplier(3)
print(double(5))
print(triple(5))