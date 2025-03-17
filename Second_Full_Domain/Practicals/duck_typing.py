class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def quack(self):  # Even though it's a dog, it has a quack method
        return "Woof! But pretending to be a duck."

def make_it_quack(animal):
    return animal.quack()  # No type checking, just calling the method

duck = Duck()
dog = Dog()

print(make_it_quack(duck))  # Output: Quack!
print(make_it_quack(dog))   # Output: Woof! But pretending to be a duck.





class Duck:
    def quack(self):
        return "Quack Quack"
    
    def walk(self):
        return "Duck is waddling"

class Dog:
    def quack(self):
        return "Woof Woof, pretending like a duck"
    
    def walk(self):
        return "Dog is walking"

def make_it_quack(obj):
    return obj.quack()

def make_it_walk(obj):
    return obj.walk()

duck = Duck()
dog = Dog()

print(make_it_quack(duck))  # Quack Quack
print(make_it_quack(dog))   # Woof Woof, pretending like a duck
print(make_it_walk(duck))   # Duck is waddling
print(make_it_walk(dog))    # Dog is walking
