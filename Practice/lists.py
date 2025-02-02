""" thislist = ['apple', 'banana', 'cherry']
[print(x) for x in thislist] """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if "a" in x]
print(newlist) """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [i for i in fruits if i!='cherry']
print(new_list) """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [x for x in fruits]
print(new_list) """


""" new_list = [i for i in range(1,11)]
print(new_list) """


""" a=[1,2,3,8,9,5,4,3,0]
new_list = [i for i in a if i<5]
print(new_list) """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [i.upper() for i in fruits]
print(new_list) """


""" fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [i if i!='banana' else 'orange' for i in fruits]
print(new_list) """


""" thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist) """


""" fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(red, yellow, *others) = fruits
print(red)
print(yellow)
print(others)  """


""" fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
a, *b, c = fruits
print(a)
print(b)
print(c) """



