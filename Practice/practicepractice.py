""" x = [4,3,7,4,2,200]
y = [1,2,3,10,2,4]

res=[]
for i in x:
    if i in y:
        res.append(i)

print(set(res)) """

""" a=[1,2,3,4,5,6,7,8,9,10]
res=list(map(lambda x: x**2, a))
print(res) """

#ethinta word um athinta lengthum ellath end
""" fruits = ["apple","banana","grapes","apple","strawberry","mango","apple","banana","banana","grapes","pineapple","Kiwi","watermelon","cherry"]
# res={i: len(i) for i in fruits}
res={x: fruits.count(x) for x in fruits}
print(res) """

""" a = [
{"name":"Angela", "age":23,"place":"newyork"},
{"name":"charlie", "age":24,"place":"america"},
{"name":"jobin", "age":23},
{"name":"Kiran", "age":43}
]

res=[]
for i in a:
    if "place" not in i.keys():
        res.append(i)

print(res) """

""" class A:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def my_add(self):
        return self.a+self.b
    
class B(A):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def my_add(self):
        return self.a+self.b
    
n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
ob1=A(n1, n2)
res1=ob1.my_add()
print(res1)

n3=int(input("Enter a number"))
n4=int(input("Enter a number"))
ob2=B(n3, n4)
res2=ob2.my_add()
print(res2) """
