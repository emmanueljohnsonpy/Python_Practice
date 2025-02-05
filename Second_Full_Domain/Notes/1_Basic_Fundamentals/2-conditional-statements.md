
# Conditional Statements in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What are conditional statements?
Conditional statements allow the program to make decisions based on certain conditions. The most common conditional statements are `if`, `elif`, and `else`.

### Syntax of `if` statement?
The `if` statement evaluates a condition and executes the block of code if the condition is `True`.  
Example:  
```python
if x > 10:
    print("x is greater than 10")
```

### What is the `elif` statement?
The `elif` (else-if) statement allows multiple conditions to be checked. It follows an `if` statement and executes if the condition is `True`.  
Example:  
```python
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
```

### What is the `else` statement?
The `else` statement executes when all preceding conditions are `False`.  
Example:  
```python
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")
```

### Can conditional statements be nested?
Yes, `if`, `elif`, and `else` statements can be nested inside each other.  
Example:  
```python
if x > 10:
    if y > 5:
        print("x is greater than 10 and y is greater than 5")
```

### How to use logical operators with conditions?
Logical operators like `and`, `or`, and `not` can combine multiple conditions.  
Example:  
```python
if x > 10 and y < 5:
    print("x is greater than 10 and y is less than 5")
```

### What are ternary operators?
Ternary operators provide a shorthand for `if-else` statements.  
Example:  
```python
result = "Yes" if x > 10 else "No"
```

---

## 📌 Summary
- Conditional statements (`if`, `elif`, `else`) make decisions based on conditions.
- Use `elif` for multiple conditions and `else` for default actions.
- Conditions can be combined using logical operators (`and`, `or`, `not`).
- Ternary operators provide a compact way to write `if-else` statements.