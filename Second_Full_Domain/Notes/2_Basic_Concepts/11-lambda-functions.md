# Python Lambda Functions: Complete Guide with Examples

## What are Lambda Functions?

### Definition
A lambda function is a small, anonymous function that can have any number of arguments but can only have one expression. They are also called "anonymous functions" or "function literals".

Syntax:
```python
lambda arguments: expression
```

### Key Characteristics
- Single expression only
- Can take multiple arguments
- Returns value automatically
- Anonymous (no name)
- Can be assigned to variables

## Basic Lambda Examples

### 1. Simple Lambda Functions
```python
# Basic addition
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Square number
square = lambda x: x**2
print(square(4))  # Output: 16

# Multiple arguments
full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))  # Output: "John Doe"
```

### 2. Lambda with Built-in Functions
```python
# With map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
# Output: [1, 4, 9, 16, 25]

# With filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# Output: [2, 4]

# With reduce()
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
# Output: 15
```

## Common Use Cases

### 1. Sorting
```python
# Sort list of tuples by second element
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
# Output: [(3, 'a'), (1, 'b'), (2, 'c')]

# Sort dictionary by value
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
```

### 2. List Comprehension with Lambda
```python
# Create function list
functions = [lambda x: x + n for n in range(4)]
results = [f(1) for f in functions]

# Create operation mapping
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y
}
```

### 3. Immediate Execution
```python
# Immediately invoked lambda
result = (lambda x: x**2)(5)  # Output: 25

# Conditional expression
result = (lambda x: "Even" if x % 2 == 0 else "Odd")(3)
```

## Advanced Patterns

### 1. Lambda with Multiple Conditions
```python
# Multiple conditions
grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else "C")

# Chained comparisons
in_range = lambda x: 0 <= x <= 100
```

### 2. Lambda with Data Processing
```python
# Process dictionary values
process_dict = lambda d: {k: v*2 for k, v in d.items()}

# Filter and transform
process_list = lambda lst: [x*2 for x in lst if x > 0]
```

### 3. Lambda as Function Arguments
```python
def apply_operation(x, y, operation):
    return operation(x, y)

# Usage
result = apply_operation(5, 3, lambda x, y: x * y)
```

## Best Practices and Tips

### 1. When to Use Lambda Functions
```python
# Good: Simple operations
sorted(names, key=lambda x: x.lower())

# Good: Quick callbacks
button.onClick(lambda e: print("Clicked!"))

# Bad: Complex operations (use regular function)
# lambda x: do_this() and do_that() and another_thing()
```

### 2. Lambda vs Regular Functions
```python
# Lambda function
multiply = lambda x, y: x * y

# Equivalent regular function
def multiply(x, y):
    return x * y
```

### 3. Common Mistakes to Avoid
```python
# Don't use lambda for multiline operations
# Bad:
lambda x: (
    temp = x * 2,
    temp + 1
)

# Instead use regular function:
def process(x):
    temp = x * 2
    return temp + 1
```

## Integration with Built-in Functions

### 1. map() with lambda
```python
# Convert temperatures
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Process multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
```

### 2. filter() with lambda
```python
# Filter out negative numbers
numbers = [-1, 0, 1, 2, -3, 4]
positive = list(filter(lambda x: x > 0, numbers))

# Filter dictionary
d = {'a': 1, 'b': 0, 'c': 2}
non_zero = dict(filter(lambda x: x[1] != 0, d.items()))
```

### 3. reduce() with lambda
```python
from functools import reduce

# Calculate factorial
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))

# Find maximum value
max_value = reduce(lambda x, y: x if x > y else y, numbers)
```

## Summary

### Key Points
1. Lambda functions are anonymous, single-expression functions
2. Perfect for simple operations and callbacks
3. Commonly used with map(), filter(), and reduce()
4. Useful for sorting and quick transformations
5. Should be kept simple and readable

### When to Use Lambda Functions
- Simple operations
- Sorting key functions
- Callbacks
- Quick data transformations
- Function arguments

### When Not to Use Lambda Functions
- Complex logic
- Multiple lines of code
- Functions that need documentation
- Reusable functions
- Error handling requirements

### Best Practices
1. Keep expressions simple
2. Use meaningful parameter names
3. Consider readability first
4. Use regular functions for complex operations
5. Avoid side effects in lambda functions