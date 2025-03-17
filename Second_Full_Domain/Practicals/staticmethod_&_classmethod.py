

# @staticmethod


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
        
print(MathOperations.add(10, 5))


# @classmethod


class Profile:
    name = "Ronaldo"
    age = 40

    @classmethod
    def change(cls, name, age):
        cls.name, cls.age = name, age
        
print(Profile.name, Profile.age)
Profile.change("Messi", 35)
print(Profile.name, Profile.age)