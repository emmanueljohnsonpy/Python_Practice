
# Loops in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What are loops in Python?
Loops are used to repeat a block of code multiple times based on a condition. The two main types of loops in Python are `for` and `while` loops.

### Syntax of `for` loop?
The `for` loop iterates over a sequence (like a list, tuple, string, or range).  
Example:  
```python
for i in range(5):
    print(i)
```

### What is `range()` function?
The `range()` function generates a sequence of numbers, commonly used with `for` loops.  
Example:  
```python
for i in range(2, 6):
    print(i)
```

### Syntax of `while` loop?
The `while` loop repeats a block of code as long as a specified condition is `True`.  
Example:  
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### What is a `break` statement?
The `break` statement is used to exit a loop prematurely when a certain condition is met.  
Example:  
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### What is a `continue` statement?
The `continue` statement skips the current iteration and moves to the next iteration in the loop.  
Example:  
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### Can loops be nested?
Yes, loops can be nested inside one another. A `for` loop can contain another `for` or `while` loop.  
Example:  
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 📌 Summary
- Loops (`for` and `while`) allow repeated execution of code.
- `for` loops iterate over a sequence; `while` loops run until a condition is `True`.
- `break` exits a loop early, and `continue` skips to the next iteration.
- Loops can be nested inside each other for complex iteration.