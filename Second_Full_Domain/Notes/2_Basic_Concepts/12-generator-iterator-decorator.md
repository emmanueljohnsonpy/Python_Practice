# Generators, Iterators, and Decorators in Python (Cornell Method)

## Questions & Key Points
1. **What is a generator in Python?**
2. **How do you create and use an iterator?**
3. **What is the purpose of a decorator?**
4. **How do these concepts improve Python programming?**

---

## Notes

### 1. Generators

A **generator** is a special type of iterator that allows you to iterate through a sequence of values lazily (one at a time). It is defined using a function and the `yield` keyword.

#### Example:
```python
# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
gen = count_up_to(5)
for num in gen:
    print(num)
```

#### Output:
```
1
2
3
4
5
```

---

### 2. Iterators

An **iterator** is an object that implements the `__iter__()` and `__next__()` methods. It allows sequential access to elements in a collection.

#### Example:
```python
class MyIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

# Using the iterator
numbers = [10, 20, 30, 40]
iter_obj = MyIterator(numbers)
for num in iter_obj:
    print(num)
```

#### Output:
```
10
20
30
40
```


#### Another example :- Python provides built-in functions iter() and next() to work with iterators manually.:
```python
iterable = [10, 20, 30]  # A list is iterable
iterator = iter(iterable)  # Get an iterator

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
# print(next(iterator))  # Raises StopIteration

```

---

### 3. Decorators

A **decorator** is a function that takes another function as an argument and extends its behavior without modifying it.

#### Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()
```

#### Output:
```
Before the function call
Hello, World!
After the function call
```

---

## Summary
- **Generators** are functions that allow lazy iteration using `yield`.
- **Iterators** implement `__iter__()` and `__next__()` to traverse collections.
- **Decorators** modify functions dynamically without changing their structure.
- These concepts enhance efficiency, reusability, and readability in Python programming.

