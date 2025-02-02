class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog and I can swim")
    def speaks(self):
        print("bow bow")

class Person:
    def speaks(self):
        print("blah blah blah")

def display(obj):
    obj.swim()
    obj.speaks()
    print("Information displayed")



d=Duck()
dog=Dog()
p=Person()
display(p)