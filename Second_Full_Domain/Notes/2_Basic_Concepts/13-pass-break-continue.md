# Pass, Break, and Continue in Python (Cornell Method)

## Questions & Key Points
1. **What is the `pass` statement in Python?**
2. **What does the `break` statement do?**
3. **How does the `continue` statement work?**
4. **When should each of these statements be used?**

---

## Notes

### 1. Pass Statement
The `pass` statement is a placeholder that does nothing when executed. It is often used in situations where a statement is syntactically required but no action needs to be taken.

#### Example:
```python
def my_function():
    pass  # Placeholder for future implementation
```

#### Use Case:
- When defining an empty function or class.
- When writing placeholder loops or conditionals.

---

### 2. Break Statement
The `break` statement is used to exit a loop immediately, even if the loop condition has not been met.

#### Example:
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

#### Output:
```
0
1
2
```

#### Use Case:
- To stop a loop when a certain condition is met.
- Useful in search operations or when an early exit is required.

---

### 3. Continue Statement
The `continue` statement skips the current iteration of a loop and moves to the next iteration.

#### Example:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### Output:
```
0
1
3
4
```

#### Use Case:
- To skip specific iterations based on a condition.
- Used when some elements should be ignored in a loop.

---

## Summary
- **Pass**: A placeholder statement that does nothing.
- **Break**: Exits the loop immediately.
- **Continue**: Skips the current iteration and moves to the next one.
- These statements provide control over the flow of loops and conditionals, making code more flexible and readable.

