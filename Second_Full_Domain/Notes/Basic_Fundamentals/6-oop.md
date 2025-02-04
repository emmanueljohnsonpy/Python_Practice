# Classes and Objects in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What is a class?
A class is a blueprint for creating objects (instances). It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have. A class encapsulates data for the object and provides methods for manipulating that data.

#### Example:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating an object (instance) of the class Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy is barking!
```

### What is an object?
An object is an instance of a class. When a class is defined, no memory is allocated. Memory is allocated only when an object is created from the class. Objects can have their own attributes and methods defined by the class.

### What is the `__init__` method?
The `__init__` method is a special method in Python classes. It is called when an object is instantiated (created). It is used to initialize the object's attributes.

#### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
print(car1.make)  # Output: Toyota
```

### What is `self` in a class?
`self` represents the instance of the class. It allows you to access the attributes and methods of the object created from the class. It is always the first parameter in instance methods and refers to the current object.

### How to create an object?
To create an object (or instance) from a class, you call the class name as if it were a function, passing the required arguments (if any).

#### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 30)
print(person1.name)  # Output: John
```

### What are instance attributes?
Instance attributes are variables that are bound to the specific instance of the class. Each object has its own copy of the instance attributes.

#### Example:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(book1.title)  # Output: 1984
print(book2.title)  # Output: To Kill a Mockingbird
```

### What are class attributes?
Class attributes are variables that are shared across all instances of a class. They are not tied to any specific object, but rather to the class itself.

#### Example:
```python
class Student:
    school = "ABC High School"  # Class attribute

    def __init__(self, name, grade):
        self.name = name  # Instance attribute
        self.grade = grade  # Instance attribute

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

print(student1.school)  # Output: ABC High School
print(student2.school)  # Output: ABC High School
```

<!-- ### How to create methods in a class?
Methods are functions defined inside a class. They define the behaviors of the objects created from the class. Instance methods take `self` as the first parameter, while class methods and static methods may use other parameters.

#### Example of a method:
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
``` -->

# Methods in Python Classes

Methods are functions defined inside a class. They define the behaviors of objects created from the class.

## Types of Methods

### 1. **Instance Method**:
- An instance method is the most common method.
- It takes `self` as the first parameter, which refers to the current instance of the class (the object created from the class).
- Instance methods typically operate on the attributes of the object (instance).

### 2. **Class Method**:
- A class method is defined using the `@classmethod` decorator.
- It takes `cls` as the first parameter, which refers to the class itself, rather than an instance.
- Class methods are used when you need to operate on the class itself, not on instances of the class.

### 3. **Static Method**:
- A static method is defined using the `@staticmethod` decorator.
- It does not take `self` or `cls` as the first parameter.
- Static methods behave like regular functions, but they belong to the class.

## Example: Instance Method, Class Method, and Static Method

```python
class Calculator:
    # Instance method
    def add(self, a, b):
        return a + b

    # Class method
    @classmethod
    def subtract(cls, a, b):
        return a - b

    # Static method
    @staticmethod
    def multiply(a, b):
        return a * b


# Create an object (instance) of the Calculator class
calc = Calculator()

# Calling the instance method on the instance
result_add = calc.add(5, 3)
print(f"Addition result: {result_add}")  # Output: 8

# Calling the class method using the class
result_subtract = Calculator.subtract(10, 3)
print(f"Subtraction result: {result_subtract}")  # Output: 7

# Calling the static method using the class
result_multiply = Calculator.multiply(4, 2)
print(f"Multiplication result: {result_multiply}")  # Output: 8
```

# **Pillars of OOP in Python**

### **1. Encapsulation**
   - **Definition**: Encapsulation is the bundling of data (variables) and methods (functions) that operate on the data within a single unit called a class. It hides the internal state of an object and only exposes a controlled interface for interaction.
   - **Purpose**: Protects the data from unauthorized access and modification.
   - **Example**:
     ```python
     class Car:
         def __init__(self, make, model):
             self.make = make
             self.model = model
             self._fuel = 100  # Private attribute

         def drive(self):
             if self._fuel > 0:
                 self._fuel -= 10  # Encapsulated fuel handling
                 print(f"Driving {self.make} {self.model}")
             else:
                 print("Out of fuel!")
     ```

### **2. Abstraction**
   - **Definition**: Abstraction involves hiding complex implementation details and showing only the essential features of an object. This is done using abstract classes or methods that define a blueprint for derived classes.
   - **Purpose**: Reduces complexity by allowing the user to interact with the object at a higher level.
   - **Example**:
     ```python
     from abc import ABC, abstractmethod

     class Animal(ABC):
         @abstractmethod
         def sound(self):
             pass

     class Dog(Animal):
         def sound(self):
             print("Woof!")
     ```

### **3. Inheritance**
   - **Definition**: Inheritance allows a new class (child) to inherit attributes and methods from an existing class (parent). This promotes code reuse and logical hierarchy.
   - **Purpose**: Enables reusability and extends functionality.

   - **Types of Inheritance in Python**:

     1. **Single Inheritance**  
        - In single inheritance, a class (child class) inherits from only one parent class.  
        - **Example**:
          ```python
          class Animal:
              def speak(self):
                  print("Animal makes a sound")

          class Dog(Animal):
              def speak(self):
                  print("Dog barks")

          dog = Dog()
          dog.speak()  # Output: Dog barks
          ```

     2. **Multiple Inheritance**  
        - In multiple inheritance, a class (child class) inherits from more than one parent class. This allows the child class to inherit attributes and methods from multiple parent classes.  
        - **Example**:
          ```python
          class Animal:
              def speak(self):
                  print("Animal makes a sound")

          class Mammal:
              def walk(self):
                  print("Mammal walks")

          class Dog(Animal, Mammal):
              def speak(self):
                  print("Dog barks")

          dog = Dog()
          dog.speak()  # Output: Dog barks
          dog.walk()   # Output: Mammal walks
          ```

     3. **Multilevel Inheritance**  
        - In multilevel inheritance, a class (child) inherits from a parent class, and another class (grandchild) inherits from that child class, forming a chain of inheritance.  
        - **Example**:
          ```python
          class Animal:
              def speak(self):
                  print("Animal makes a sound")

          class Dog(Animal):
              def speak(self):
                  print("Dog barks")

          class Puppy(Dog):
              def speak(self):
                  print("Puppy whines")

          puppy = Puppy()
          puppy.speak()  # Output: Puppy whines
          ```

     4. **Hierarchical Inheritance**  
        - In hierarchical inheritance, multiple child classes inherit from a single parent class.  
        - **Example**:
          ```python
          class Animal:
              def speak(self):
                  print("Animal makes a sound")

          class Dog(Animal):
              def speak(self):
                  print("Dog barks")

          class Cat(Animal):
              def speak(self):
                  print("Cat meows")

          dog = Dog()
          cat = Cat()
          dog.speak()  # Output: Dog barks
          cat.speak()  # Output: Cat meows
          ```

     5. **Hybrid Inheritance**  
        - Hybrid inheritance is a combination of two or more types of inheritance. This can occur when multiple inheritance is mixed with other forms such as multilevel or hierarchical inheritance.  
        - **Example**:
          ```python
          class Animal:
              def speak(self):
                  print("Animal makes a sound")

          class Mammal:
              def has_hair(self):
                  print("Mammal has hair")

          class Dog(Animal, Mammal):
              def speak(self):
                  print("Dog barks")

          dog = Dog()
          dog.speak()        # Output: Dog barks
          dog.has_hair()     # Output: Mammal has hair
          ```

   - **Key Concepts**:
     - **Method Overriding**: Child classes can override methods from parent classes to provide their own specific implementation.
     - **`super()` Function**: Used to call a method from the parent class, enabling method chaining and code reuse.
     - **Is-a Relationship**: Inheritance establishes an "is-a" relationship, where the child class is a specialized version of the parent class.

   - **Summary**:
     - **Single Inheritance** involves one parent class.
     - **Multiple Inheritance** involves multiple parent classes.
     - **Multilevel Inheritance** involves a chain of inheritance.
     - **Hierarchical Inheritance** involves multiple child classes inheriting from one parent class.
     - **Hybrid Inheritance** combines multiple inheritance types.


### **4. Polymorphism**
   - **Definition**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. The most common use of polymorphism is method overriding, where a subclass provides a specific implementation of a method defined in the superclass.
   - **Purpose**: Allows flexibility and the ability to interact with different types in a unified manner.
   - **Example**:
     ```python
        class Animal:
            def speak(self):
                print("Animal makes a sound")

        class Dog(Animal):
            def speak(self):  # Overriding the parent method
                print("Dog barks")
        # Creating objects
        animal = Animal()
        dog = Dog()

        # Calling the speak method
        animal.speak()  # Output: Animal makes a sound
        dog.speak()     # Output: Dog barks (Overridden method)
     ```

## 📌 **Summary**
- Classes are blueprints for creating objects, and objects are instances of those classes.
- The `__init__` method initializes an object's attributes when it is created.
- `self` refers to the current object in instance methods and allows access to its attributes and methods.
- Instance attributes belong to the object, while class attributes are shared by all instances of the class.
- Methods are functions defined inside a class, and inheritance allows classes to inherit from other classes.
- Polymorphism allows methods to have the same name but behave differently depending on the object.

