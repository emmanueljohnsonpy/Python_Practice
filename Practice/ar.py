""" class adding:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a +self.b
abc = adding(int(input("Enter the number")),int(input("Enter the number")))  
y = abc.add()
print(y) """

class adding:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
class summ(adding):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b  

a=adding(int(input("enter")),int(input("enter")))
y=a.add()
print(y)

b = summ(int(input("Enter a number")),int(input("Enter a number"))) 
z = b.add()
print(z)

#map maajid

""" a = [1,2,3,4,5,6,7,8,9,10]
b = map(lambda x : x*x ,a)
print(list(b)) """

#filter maajid

""" a = [1,2,3,4,5,6,7,8,9,10]
c = filter(lambda x: x%2==0,a)
print(list(c))  """

#maajid dict
""" a = ["apple","orenge","banana","grape"]
b = {i:len(i) for i in a}
print(b) """

#sum of 2 valuse using class constructor method maajid
""" class addr:
    def _init_(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
adding = addr(10,30)
res = adding.add()
print(res) """

#common elemnts from 2 lists maajid


#fibinocci series using recursion maajid

""" n=5
res=[0,1]
for i in range(2,n):
    next=res[-1]+res[-2]
    res.append(next)
print(res) """



#adding values in tuple maajid
# t = (1,2,3,4,5)
# t = t+(6,)
# print(t)

""" def facto(n):
    if n==0:
        return 1
    else:
        return n* facto(n-1)
n = 5
print(facto(n)) """

a="ABCDEFGGGG"
print(a.replace("G","yo"))