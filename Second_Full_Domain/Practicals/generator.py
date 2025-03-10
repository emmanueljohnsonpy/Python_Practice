

# generator implimentation

def my_generator():
    yield 1
    yield 2
    yield 3
    
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))


# Using Generators in a Loop

def my_generator(n):
    count = 0
    while count <= n:
        yield count
        count += 1
        
for num in my_generator(7):
    print(num)