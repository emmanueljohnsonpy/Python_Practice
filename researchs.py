""" def myfunc(*args):
    n=len(args)
    print("sum", sum(args))
    print("average", sum(args)/n)

myfunc(1,2,3) """


""" s = "aabbca"
b=""
count = 1
s+="0"
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        b+=s[i]
        b+=str(count)
        count=1
print(b)
 """

#map()
""" def sqr(x):
    return x*x
n = [1,2,3,4,5]
s = map(sqr, n)
s1 = list(s)
print(s1)    
 """
#removing dict keys
""" d = {'a':1,'b':2}
for i in list(d.keys()):
    del d[i]
print(d) """


#map
""" n=[3,4,2,5,6]
res=list(map(lambda x:x*x,n))
print(res) """

#reduce
""" from functools import reduce
n=[1,2,3,4,5]
a=reduce(lambda x,y: x+y,n)
print(a) """

#filter
""" a=[1,2,3,4,5]
res=list(filter(lambda i:i%2==0, a))
print(res) """


""" class animal:
    def metod(self):
        print("good sound")
class dog(animal):
    def metod(self):
        print("bad sound")
b = dog()  
b.metod() 
a = animal()
a.metod()
 """

""" li = ["a","b","c","d","e","f"]
for i,y in enumerate(li):
    print(i,y) """

""" #unpack a list
l = [1,2,3,4,5,6,7]
print(*l)
# 
def sum(a,b,c):
    return a+b+c
a = [10,20,10]
print(sum(*a))    """


""" a=[1,2,3,4,5,6,7,8,9,10]
res=[x **2 if x%2 ==0 else x**3 for x in a]
print(res) """

""" a=0
print("pos") if a>0 else print("zero") if a==0 else print("neg") """

""" dict={1:"mango",2:"apple",3:"orange"}
res={x:len(y) for x, y in dict.items()}
print(res) """

dict1 = {
    'one' : 6,
    'two' : 8,
    'three': 9,
    'four' : 2
}

for k1, v1 in dict1.items():
    for k2, v2 in dict1.items():
        if v2>v1:
            temp=dict1[k1]
            dict1[k1]=dict1[k2]
            dict1[k2]=temp
print(dict1)
            





    