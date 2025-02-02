""" my_list=[1, 2, 3, 4, 5]

# Basic list operations

first_element=my_list[0]
last_element=my_list[-1]
print(first_element)
print(last_element)
my_list[0]=10
print(my_list)
my_list.append(6)
my_list.insert(1, 20)
print(my_list)
my_list.remove(20)
print(my_list)
popped_element=my_list.pop()
print(popped_element)
print(my_list)

# Slicing

sub_list=my_list[1:4]
print(sub_list)
reverse_list=sub_list[::-1]
print(reverse_list)

# List Methods

my_list.sort()
print(my_list)
sorted_list=sorted(my_list)
print(sorted_list)
index=my_list.index(3)
print(index)
count=my_list.count(2)
print(count)
my_list.extend([7,8,9])
print(my_list)

# Common use cases

squares=[x**2 for x in range(10)]
print(squares)
even_numbers=[x for x in my_list if x%2==0]
print(even_numbers)
doubled=[x*2 for x in my_list]
print(doubled)

# Iterating through a list

for item in my_list:
    print(item)
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# Other list operations

copy_list=my_list.copy()
print(copy_list)
another_copy=my_list[:]
print(another_copy)
my_list.clear()
print(my_list) """

""" # Creating dictionaries

my_dict={'key1': 'value1', 'key2': 'value2'}
print(my_dict)
empty_dict={}
print(empty_dict)

# Accessing Elements

value1=my_dict['key1']
print(value1)
value2=my_dict.get('key2')
print(value2)
nonexistent_value=my_dict.get('key3', 'default_value')
print(nonexistent_value)

# Modifying Elements

my_dict['key1']='New Value'
my_dict['key3']='Value3'
print(my_dict)

# Removing Elements

del my_dict['key1']
print(my_dict)
a=my_dict.pop('key2')
print(my_dict)
b=my_dict.popitem()
print(my_dict)

# Checking for keys

is_key1_in_dict='key1' in my_dict
print(is_key1_in_dict)

# Iterating through a dictionary

my_dict={'key1': 'value1', 'key2': 'value2'}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Dictionary Methods

my_dict.update({'key3' : 'value3', 'key4': 'value4'})
print(my_dict)
new_dict=my_dict.copy()
print(my_dict)
keys=list(my_dict.keys())
print(keys)
values=list(my_dict.values())
print(values)
my_dict.clear()
print(my_dict)

# Dictionary Comprehensions

squared_numbers={x: x**2 for x in range(10)}
print(squared_numbers) """

# Do more practicals with dict

""" elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_elements={}
for v in elements:
    if v in freq_elements:
        freq_elements[v]+=1
    else:
        freq_elements[v]=1

print(freq_elements) """

""" dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
res=dict1.copy()

for k, v in dict2.items():
    if k in res:
        res[k]+=v
    else:
        res[k]=v

print(res)
 """

""" def sampledec(func):
    def wrapper():
        print("Loo")
        func()
        print("Lo")
    return wrapper

@sampledec
def samplefunc():
    print("hai")

samplefunc() """

""" def simplegen():
    yield 1
    yield 2
    yield 3

res=simplegen()
for i in res:
    print(i) """


""" for i in range(5):
    print(i)

i=0
while i<5:
    print(i)
    i+=1 """

""" my_list = [1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 9, 1]
seen=set()
dup=set()
for i in my_list:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(dup) """

""" numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_odd=["even" if i%2==0 else "odd" for i in numbers]
print(even_odd) """

""" my_string = "hello world"
res={}
for i in my_string:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res) """

""" from collections import Counter
my_string = "hello world"
res=Counter(my_string)
print(dict(res)) """

""" class Point:
    def __init__(self, a, b):
        self.a=a 
        self.b=b
    def __add__(self, other):
        return Point(self.a+other.a, self.b+other.b)
    def __str__(self):
        return f"Point({self.a},{self.b})"
    
a=Point(1, 2)
b=Point(3, 4)
print(a+b) """

""" my_list = ['Hello', 'world', 'this', 'is', 'Python']
res=" ".join(my_list)
print(res) """

""" my_dict = {'a': 1, 'b': 2, 'c': 3}
res={v: k for k, v in my_dict.items()}
print(res) """

""" my_dict = {'a': 10, 'b': 20, 'c': 30}
res=max(my_dict, key=my_dict.get)
print(res) """

