
# Error Handling in Python

Error handling in Python is done using `try`, `except`, `else`, and `finally` blocks. Here's how each component works:

1. **`try` block**: Contains the code that might raise an error.
2. **`except` block**: Catches and handles the error if one occurs in the `try` block.
3. **`else` block**: Runs if no error occurs in the `try` block.
4. **`finally` block**: Executes no matter what, whether an error occurred or not.

## Basic Example:
```python
try:
    # Code that might raise an error
    x = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    # Code to handle the error
    print(f"Error: {e}")
else:
    # Code to execute if no error occurred
    print("No error occurred!")
finally:
    # Code that always runs
    print("This will always run.")
```

### Output:
```
Error: division by zero
This will always run.
```

## Multiple `except` blocks:
You can handle different exceptions separately.

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("End of error handling.")
```

## Raising Exceptions:
You can raise exceptions manually using the `raise` keyword.
```python
def validate_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return True

try:
    validate_age(16)
except ValueError as e:
    print(e)
```

### Output:
```
Age must be 18 or older.
```