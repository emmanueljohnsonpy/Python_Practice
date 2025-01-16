#Create a lambda function that adds 20 to a given number.

""" a=lambda x: x+20
res=a(5)
print(res) """

#Write a lambda function that multiplies two numbers together and returns the product.

""" a = lambda x,y: x*y
res=a(5, 6)
print(res) """

#Doubling Numbers

""" a=[1,2,3,4,5]
a=map(lambda x: x*2 , a)
print(list(a)) """

#Applying Functions to Multiple Lists

""" a=[1,2,3,4,5]
b=[6,7,8,9,10]
res=list(map(lambda x,y: x+y , a , b))
print(res) """

#Modifying Strings

""" words=['sat', 'bat', 'cat', 'map']
res=list(map(list, words))
print(res) """

#using filter() with a lambda function to filter out even numbers

""" a=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x: x%2==0, a))
print(res) """

#Summing all numbers in a list

""" from functools import reduce 

a=[1,2,3,4,5]
res=reduce(lambda x,y: x+y, a)
print(res) """

#adding a value in tuple

""" a=(1,2,3,4,5)
b=6
res=a+(b,)
print(res) """

#2 list thannitt common elements

""" a=[1,2,3,4,5]
b=[5,6,7,8,9]
res=[]
for i in a:
    if i in b:
        res.append(i)
    
print(res) """

#List I'll dictionary aahn elements.. Athill motham 4 dictionary. Athill 2 key value pair illath mathram puthiya list I'll add cheyya
""" L=[{'a' : 1 , 'b' : 2},
{'c' : 3 , 'c' : 4},
{'e' : 5, 'f' : 6, 'g' : 7},
{'h' : 8, 'i' : 9, 'j' : 10}]
res=[]
for i in L:
    if len(i)==2:
        res.append(i)

print(res) """

""" l = ['apple', 'orange', 'grapes', 'pineapple', 'strawberry']
res={i: len(i) for i in l}
print(res) """


