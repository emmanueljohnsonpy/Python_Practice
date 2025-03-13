class Parent:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("Bark Bark")
        
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def bark(self):
        super().bark()
        
obj = Child("Ronaldo", 40)
print(obj.name, obj.age)
obj.bark()