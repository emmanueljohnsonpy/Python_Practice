""" class adding:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
num1=int(input("enter a number"))
num2=int(input("enter a number"))
obj=adding(num1, num2)
res=obj.addition()
print(res) """

class Parent:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def adding(self):
        return self.a+self.b

class Child(Parent):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def adding(self):
        return self.a+self.b
    
obj=Child(20, 10)
res=obj.adding()
print(res)    



