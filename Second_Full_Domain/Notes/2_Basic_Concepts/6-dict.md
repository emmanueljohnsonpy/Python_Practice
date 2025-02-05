# Python Dictionaries: Complete Guide with Q&A and Methods

## Fundamental Questions & Answers

### Q1: What is a Python dictionary?
**A:** A Python dictionary is an ordered collection of key-value pairs. Each key must be unique and immutable (strings, numbers, or tuples), while values can be of any type, including other dictionaries.

```python
# Example dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

### Q2: Why use dictionaries?
**A:** Dictionaries are used because they:
- Provide fast lookup using keys (O(1) time complexity)
- Allow meaningful associations between keys and values
- Can store complex data structures
- Are mutable and flexible
- Support dynamic addition and removal of items

### Q3: How do you access values in a dictionary?
**A:** Values can be accessed using:
1. Square bracket notation with key
2. get() method
3. Keys, values, or items views

```python
person = {"name": "John", "age": 30}
name = person["name"]          # Using brackets
age = person.get("age")       # Using get()
age = person.get("salary", 0) # With default value
```

### Q4: What's the difference between dict.get() and direct access?
**A:**
- Direct access (`dict[key]`) raises KeyError if key doesn't exist
- `get()` returns None (or specified default) if key doesn't exist

```python
# Direct access
try:
    value = person["salary"]  # Raises KeyError if not found
except KeyError:
    value = 0

# Using get()
value = person.get("salary", 0)  # Returns 0 if not found
```

## Complete Dictionary Methods Reference

### 1. Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# From key-value pairs
dict1 = {"a": 1, "b": 2}

# Using dict() constructor
dict2 = dict(name="John", age=30)

# From list of tuples
dict3 = dict([("a", 1), ("b", 2)])

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

### 2. Adding and Updating Elements
```python
# Update single item
person["age"] = 31

# Update multiple items
person.update({"age": 32, "city": "Boston"})

# Using update() with keyword arguments
person.update(age=33, country="USA")

# setdefault(): Set key with default if not exists
value = person.setdefault("age", 30)  # Returns existing or default
```

### 3. Removing Elements
```python
# pop(): Remove and return value
age = person.pop("age")  # Removes and returns value
age = person.pop("age", None)  # With default if key missing

# popitem(): Remove and return last item
last_item = person.popitem()  # Returns tuple (key, value)

# clear(): Remove all items
person.clear()

# del statement: Remove specific key
del person["age"]
```

### 4. Accessing and Viewing
```python
# keys(): Get view of keys
keys = person.keys()

# values(): Get view of values
values = person.values()

# items(): Get view of key-value pairs
items = person.items()

# get(): Safe access with default
value = person.get("key", default_value)

# Copy dictionary
copy_dict = person.copy()  # Shallow copy
import copy
deep_copy = copy.deepcopy(person)  # Deep copy
```

### 5. Dictionary Information
```python
# Length of dictionary
size = len(person)

# Check key existence
exists = "name" in person
exists = person.has_key("name")  # Python 2.x only

# Check if dictionary is empty
is_empty = not bool(person)
```

## Common Operations and Patterns

### Dictionary Comprehension
```python
# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in dict1.items() if v > 0}
```

### Merging Dictionaries
```python
# Python 3.5+
merged = {**dict1, **dict2}

# Using update()
merged = dict1.copy()
merged.update(dict2)
```

### Nested Dictionaries
```python
nested = {
    "person1": {
        "name": "John",
        "age": 30
    },
    "person2": {
        "name": "Jane",
        "age": 25
    }
}
```

## Best Practices and Common Patterns

### 1. Safe Key Access
```python
# Using get()
value = dict.get("key", default_value)

# Using setdefault()
value = dict.setdefault("key", default_value)

# Using defaultdict
from collections import defaultdict
d = defaultdict(list)  # Default value is empty list
```

### 2. Dictionary Views
```python
# Iterate over keys and values together
for key, value in dict.items():
    print(f"{key}: {value}")

# Check if all values meet condition
all_adults = all(age >= 18 for age in ages.values())
```

## Summary of Key Points

1. **Basics**
   - Dictionaries store key-value pairs
   - Keys must be unique and immutable
   - Values can be of any type
   - Unordered in Python < 3.7, ordered by insertion after

2. **Key Methods**
   - `get()` for safe access
   - `update()` for multiple updates
   - `pop()` and `popitem()` for removal
   - `keys()`, `values()`, `items()` for views

3. **Important Operations**
   - Dictionary comprehension for creation
   - Merging dictionaries
   - Nested structures
   - View objects for iteration

4. **Best Practices**
   - Use `get()` or `setdefault()` for safe access
   - Consider `defaultdict` for special cases
   - Use dictionary comprehension for clarity
   - Keep keys simple and meaningful

5. **Common Gotchas**
   - KeyError on missing keys with direct access
   - Mutable values can change unexpectedly
   - Shallow vs deep copy considerations
   - Memory usage with large dictionaries

Remember:
- Dictionaries are optimized for fast lookup
- Keys should be meaningful and descriptive
- Consider memory usage with large datasets
- Use appropriate methods for better code readability