""" def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) """

# Python enhancement proposal
""" 
a="print('hai')"
exec(a) """

""" a=56
print(id(a)) """

""" def square(x):
        return x * x

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each item in the list
squared_numbers = map(square, numbers)
print(list(squared_numbers))  """

# a = [False,False]
# result = all(a)
# print(result) # Output: True

x=lambda a:a[-1]
a=[1,2,3]
print(x(a))

