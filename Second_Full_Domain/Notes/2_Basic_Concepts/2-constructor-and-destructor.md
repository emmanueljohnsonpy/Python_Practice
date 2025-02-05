
# Python Constructors and Destructors

## Constructor (`__init__`)

A constructor is a special method that is automatically called when a new instance of a class is created. It is used to initialize the object's attributes or perform setup operations. The constructor method in Python is defined using the `__init__` method.

### Syntax:
```python
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        print("Constructor called!")
```

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {self.name}, {self.age}")

# Creating an instance of Person
p = Person("John", 25)
```

Output:
```
Person object created: John, 25
```

## Destructor (`__del__`)

A destructor is a special method that is called when an object is about to be destroyed or deleted. In Python, the `__del__` method is used as a destructor. It is typically used for cleanup operations, such as closing files or releasing resources.

### Syntax:
```python
class MyClass:
    def __del__(self):
        print("Destructor called!")
```

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {self.name}, {self.age}")

    def __del__(self):
        print(f"Destructor called for {self.name}")

# Creating and deleting an instance of Person
p = Person("John", 25)
del p
```

Output:
```
Person object created: John, 25
Destructor called for John
```

## Key Notes:

- The `__init__` constructor is automatically invoked when an object is created, while `__del__` is automatically called when an object is deleted.
- In Python, the `__del__` method may not be called immediately when an object is deleted because Python uses garbage collection, which means objects are destroyed when the reference count drops to zero.