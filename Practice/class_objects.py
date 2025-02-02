""" class MyClass:
    x=5

p1=MyClass()
print(p1.x) """

""" class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("automatically exucuted")
    
p1=Person("messi", 36)
print(p1.name)
print(p1.age) """


""" class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age}"

p1=Person("Ronaldo", 37)
print(p1) """


""" class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print(f"{self.name} is {self.age}")

p1=Person("Ronaldo",37)
p1.age=40
del p1.age
p1.myfunc()
 """









