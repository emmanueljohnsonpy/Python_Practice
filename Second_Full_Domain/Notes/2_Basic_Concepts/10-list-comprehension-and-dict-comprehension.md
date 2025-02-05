# Python Comprehensions: Complete Guide with Examples

## List Comprehensions

### Basic Syntax
```python
[expression for item in iterable if condition]
```

### 1. Simple List Comprehension
```python
# Basic: Create list of squares
squares = [x**2 for x in range(10)]
# Equivalent to:
squares = []
for x in range(10):
    squares.append(x**2)

# With condition: Even squares only
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 2. List Comprehension with String Operations
```python
# Convert strings to uppercase
names = ['john', 'jane', 'bob']
upper_names = [name.upper() for name in names]

# Get length of each word
words = ['hello', 'world', 'python']
lengths = [len(word) for word in words]

# Extract first character
first_chars = [word[0] for word in words if word]
```

### 3. Nested List Comprehension
```python
# Create matrix
matrix = [[i + j for j in range(3)] for i in range(3)]
# Result: [[0,1,2], [1,2,3], [2,3,4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested for num in sublist]
# Result: [1, 2, 3, 4, 5, 6]
```

### 4. List Comprehension with Conditional Logic
```python
# If-else in comprehension
numbers = [-4, -2, 0, 2, 4]
abs_values = [num if num >= 0 else -num for num in numbers]

# Multiple conditions
filtered = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
```

## Dictionary Comprehensions

### Basic Syntax
```python
{key_expression: value_expression for item in iterable if condition}
```

### 1. Simple Dictionary Comprehension
```python
# Create dictionary of squares
squares = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16}
```

### 2. Dictionary Comprehension from Lists
```python
# Create dict from two lists
names = ['apple', 'banana', 'cherry']
prices = [0.99, 0.45, 1.29]
fruit_prices = {name: price for name, price in zip(names, prices)}

# Create dict from list with enumerate
indexed = {index: value for index, value in enumerate(names)}
```

### 3. Dictionary Comprehension with Transformations
```python
# Transform keys and values
prices = {'apple': 0.99, 'banana': 0.45, 'cherry': 1.29}
scaled_prices = {k.upper(): v*2 for k, v in prices.items()}

# Filter and transform
cheap_fruits = {k: v for k, v in prices.items() if v < 1.00}
```

### 4. Nested Dictionary Comprehension
```python
# Create nested dictionary
matrix = {i: {j: i*j for j in range(3)} for i in range(3)}
# Result: {0: {0:0, 1:0, 2:0}, 1: {0:0, 1:1, 2:2}, 2: {0:0, 1:2, 2:4}}
```

## Set Comprehensions

### Basic Syntax
```python
{expression for item in iterable if condition}
```

### Examples
```python
# Create set of squares
square_set = {x**2 for x in range(5)}

# Unique characters in string
unique_chars = {char.lower() for char in "Hello World"}
```

## Common Patterns and Best Practices

### 1. Filtering Patterns
```python
# Filter None values
valid_items = [x for x in items if x is not None]

# Filter by type
numbers = [x for x in mixed_list if isinstance(x, (int, float))]

# Complex filtering
adults = {name: age for name, age in people.items() if age >= 18}
```

### 2. Transformation Patterns
```python
# Convert types
numbers = [float(x) for x in string_numbers]

# Format strings
formatted = [f"{name}: {score}" for name, score in results]

# Multiple transformations
processed = {k: v.strip().lower() for k, v in data.items()}
```

### 3. Performance Considerations
```python
# Good: Single comprehension
squares = [x**2 for x in range(1000)]

# Bad: Nested loops in comprehension when not needed
# Use regular loops instead if logic is complex
```

## Best Practices

1. **Readability First**
   - Keep comprehensions simple and readable
   - Break complex comprehensions into multiple steps
   - Use regular loops for complex logic

2. **When to Use**
   - Simple transformations
   - Basic filtering
   - Creating new collections from existing ones

3. **When Not to Use**
   - Complex conditions
   - Multiple nested loops
   - Side effects

4. **Common Mistakes to Avoid**
   ```python
   # Too complex (hard to read)
   result = [x for x in range(10) if x > 5 if x % 2 == 0 if x % 3 == 0]
   
   # Better as regular loop
   result = []
   for x in range(10):
       if x > 5 and x % 2 == 0 and x % 3 == 0:
           result.append(x)
   ```

## Summary

1. **Benefits of Comprehensions**
   - More concise code
   - Often more readable
   - Can be more efficient
   - Expressive and Pythonic

2. **Types of Comprehensions**
   - List comprehensions: `[expr for item in iterable]`
   - Dict comprehensions: `{key: value for item in iterable}`
   - Set comprehensions: `{expr for item in iterable}`

3. **Key Features**
   - Can include conditions (filtering)
   - Support nested iterations
   - Can transform elements
   - Can use complex expressions

4. **Usage Guidelines**
   - Keep it simple
   - Prioritize readability
   - Consider performance for large datasets
   - Use appropriate type for the task