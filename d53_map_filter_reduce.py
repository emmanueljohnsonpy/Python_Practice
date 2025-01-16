def cube(x):
    return x*x*x
# MAP

""" a=[1,2,3,4,5]
res=list(map(cube, a))
print(res) """

# FILTER

""" a=[1,2,3,4,5]
def filter_func(x):
    return x>2

res=list(filter(filter_func,a))
print(res) """

# REDUCE
from functools import reduce
a=[1,2,3,4,5]
def mysum(x,y):
    return x+y

res=reduce(mysum,a)
print(res)