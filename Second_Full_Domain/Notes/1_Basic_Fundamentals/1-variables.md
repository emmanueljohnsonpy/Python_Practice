# Variables in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What is a variable?

A variable is a container for storing data values. In Python, variables do not require explicit declaration.

### How to declare a variable?

Assign a value using `=`. Example:

```python
x = 10
```

### Do variables have data types?

Yes, but Python dynamically assigns types. Example:

```python
x = 10  # int
y = "Hello"  # str
```

### Rules for naming variables?

1. Must start with a letter or `_`.
2. Cannot start with a number.
3. Can only contain letters, numbers, and `_`.
4. Case-sensitive (`Age` ≠ `age`).

### How to check a variable's type?

Use `type(variable)`. Example:

```python
x = 10
print(type(x))  # Output: <class 'int'>
```

### Can variables change types?

Yes, Python allows dynamic typing:

```python
x = 10  # int
x = "Hello"  # Now it's a string
```

### What is variable unpacking?

Assign multiple values at once:

```python
a, b, c = 1, 2, 3
```

### What are global and local variables?

- **Local:** Defined inside a function, accessible only within that function.
- **Global:** Declared outside any function, accessible everywhere. Use `global` keyword inside functions.  
  Example:

```python
x = 10  # Global variable

def my_function():
    global x
    x = 20  # Modifies global x

my_function()
print(x)  # Output: 20
```

---

## 📌 Summary

- Variables store values without explicit declaration.
- Python dynamically assigns data types.
- Variable names must follow specific rules.
- `type()` checks data type.
- Python allows **dynamic typing** and **multiple assignments**.
- **Global and local variables** control scope.
