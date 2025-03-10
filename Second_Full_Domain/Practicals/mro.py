""" class GrandParent:
    def greet(self):
        print("hai from grandparent")
    
class Parent:
    def greet(self):
        print("hai from parent")

class Child(Parent, GrandParent):
    pass

print(Child.__mro__)
print(Child.mro()) """


class A:
    def greet(self):
        print("Hello from A")
        
class B(A):
    def greet(self):
        print("Hello from B")
        
class C(A):
    def greet(self):
        print("Hello from C")
        
class D(B, C):
    pass

d = D()
d.greet()
print(D.mro())