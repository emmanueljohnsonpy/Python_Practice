#single inheritance

""" class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")
    
obj=Child()
obj.func1()
obj.func2() """

#multiple inheritance

""" class Parent1:
    def func1(self):
        print("This is function 1")

class Parent2:
    def func2(self):
        print("This is function 2")

class Child(Parent1, Parent2):
    def func3(self):
        print("This is function 3")

obj=Child()
obj.func1()
obj.func2()
obj.func3() """

#Multilevel inheritance

""" class Grandparent:
    def func1(self):
        print("This is function 1")
    
class Parent(Grandparent):
    def func2(self):
        print("This is function 2")

class Child(Parent):
    def func3(self):
        print("This is function 3")

obj=Child()
obj.func1()
obj.func2()
obj.func3() """

#Hierarchical inheritance

""" class Parent:
    def func1(self):
        print("This is function 1")

class Child1(Parent):
    def func2(self):
        print("This is function 2")

class Child2(Parent):
    def func3(self):
        print("This is function 3")

obj1=Child1()
obj2=Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3() """

#hybrid inheritance

""" class Parent1:
    def func1(self):
        print("This is function 1")
    
class Parent2:
    def func2(self):
        print("This is function 2")

class Child1(Parent1):
    def func3(self):
        print("This is function 3")

class Child2(Parent1, Parent2):
    def func4(self):
        print("This is function 4")

obj1=Child1()
obj2=Child2()
obj1.func1()
obj1.func3()
obj2.func1()
obj2.func2()
obj2.func4() """

