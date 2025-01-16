# find duplicate element from list without modifying the list


""" elem=[1,2,3,4,5,2,3,7,8]
s=set()
a=[]
for i in elem:
    if i in s:
        a.append(i)
    else:
        s.add(i) """


# Key value pairs from string , Key will be elements in the string and value will be the counts of each element in the string

""" IMP
a="Ronaldo"
s={}
for i in a:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
print(s)
"""

# Lambda function to return last element of list

# sample two sum

"""
n1=4
n2=7
x=lambda n1,n2:n1+n2
print(x(n1,n2))
"""

# returning last element

"""
a=[1,2,3,4,5]
x=lambda a:a[-1]
print(x(a))
"""

# variadic function to return sum and average of all args

"""
def sample(*args):
    s=sum(*args)
    avg=s/len(*args)
    return s, avg

a=[1,2,3,4,5,6,7]
s, avg =sample(a)
print(s)
print(avg)
"""

# second largest in a string
# using map (,)
""" 
a="12,78,45,90"
res=a.split("")
ints = list(map(int, res))
ints.sort()
print(ints[-2])
"""

# using list comprehension (,)

"""
a="10,25,30,56"
list1=a.split(",")
a=[int(i) for i in list1]
a.sort()
print(a[-2])
"""

# using list comprehension without (,)

""" a="247548339"
l=0
for i in range(len(a)):
    if int(a[i])>l:
        l=int(a[i])
print(l) """
"""
largest=sorted(set(int(i) for i in a))[-1]
print(largest)
"""

""" elem=[1,2,3,4,5,2,3,7,8]
s=set()
a=[]
for i in elem:
    if i in s:
        a.append(i)
    else:
        s.add(i)

print(a) """

# Type annotation for functions

""" def a(a:int,b:int)->int:
    return a+b

print(a(5,4.5)) """

# extracting string from list

""" a=[1,2,3,'a','b']
b=[i for i in a if type(i)==str]
print(b) """

# even or odd in list comprehension

""" a=[1,2,3,4,5,6,7]
a=["even" if i % 2 == 0 else "odd" for i in a]
print(a) """

# for else

""" for i in range(1,6):
    print(i)
    if i==3:
        break
else:
    print("for loop completed") """


# print(a:=45)

""" def facto(r):
    r=1
    for i in range(1,5+1):
        r=r*i
    return r

print(facto(5)) """

""" def facto(x):
    if x==1:
        return 1
    return x*facto(x-1) """

""" result=facto(5)
print(result)

for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(j,end="")
    print() """

""" list1=['apple','orange','grapes']
list2=['grapes','banana','lemon']
list3=list1+list2
res=set(list3)
print(res) """




# fibonacci series
# n=10
# a=[0,1]
# for i in range(2,n):
#     next_n=a[-1]+a[-2]
#     a.append(next_n)
# print(a)

# a="hello how are you"
# k=2
# list1=a.split(" ")
# list1.pop(k)
# z="~".join(list1)
# print(z)


# nums = [2,5,6,9,10]
# list1=[]
# a=min(nums)
# b=max(nums)
# i=1
# while i<=b:
#     if i%a==0 and i%b==0:
#         list1.append(i)
#     i+=1
# print(list1[-1])
# a=["sujith","emmanuel","aston"]

# from itertools import zip_longest

# list1 = [10, 20, 30, 40, 400]
# list2 = [100, 200, 300, 400, 10]

# l3 = [x for x, y in zip(list1, list2) if x == y]

# print(l3)


# a=[1,4,3,7,6,9]
# for i in range(len(a)//2):
#     temp=a[i]
#     a[i]=a[len(a)-i-1]
#     a[len(a)-i-1]=temp
# print(a)

# l1=0
# l2=0
# for i in range(len(a)):
#     if l1<a[i]:
#         l2=l1 
#         l1=a[i]
# print(l2)

a=[12,34,23,56,78]
b=[12,45,56,34,90]
res=[]
for i in a:
    if i in b:
        res.append(i)
print(res)
