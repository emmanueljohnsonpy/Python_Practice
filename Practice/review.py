# l1=[{"name":"Amrutha","age":21,"place":"Wayanad"},
#     {"name":"Ronaldo","age":37,"place":"Portugal"},
#     {"name":"Messi","age":35},
#     {"name":"Neymar","age":25}]
# a=[]
# for i in range(len(l1)):
#     if len(l1[i]) == 2:
#         a.append(l1[i])
# print(a)

#method overriding
""" class adding:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
class summ(adding):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
a = adding(int(input("Enter a number")),int(input("Enter a number")))
b = a.add() 
print(b)  
c = summ(int(input("Enter a number")),int(input("Enter a number")))
d = c.add()
print(d)    """ 


""" l = ["apple","orenge","red","black"]
d = {i:len(i) for i in l} 
print(d)
 """


# l = [1,2,3,4]
# # m = l
# y = l.copy()
# print(y)


#constructor

class myclass:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def sum(self):
        res=self.a+self.b
        return print(res)
    
obj=myclass(10,5)
obj.sum()
