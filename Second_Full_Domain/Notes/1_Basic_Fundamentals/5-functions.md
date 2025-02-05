# Functions in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What is a function?
A function is a block of reusable code that performs a specific task. It allows for modular code, better organization, and easier maintenance. Functions can take inputs (parameters) and return outputs (values).

### How to define a function?
A function is defined using the `def` keyword, followed by the function name and parentheses. You can pass parameters inside the parentheses, and the function body is indented.  
Example:
```python
def greet(name):
    print(f"Hello, {name}!")
```

### How to call a function?
To call a function, you simply use the function name followed by parentheses. If the function takes parameters, you pass the arguments inside the parentheses.  
Example:
```python
greet("Alice")  # Output: Hello, Alice!
```

### What are function parameters?
Parameters are variables listed inside the parentheses in a function definition. They allow the function to accept input values.

### What are function arguments?
Arguments are the values passed to the function when it is called. These values are used to populate the corresponding parameters.

### What is a return statement?
The `return` statement is used to exit a function and pass a result back to the caller. If no `return` statement is used, the function returns `None` by default.  
Example:
```python
def add(a, b):
    return a + b
result = add(3, 4)  # Output: 7
```

### What are default parameters?
Default parameters are parameters that take default values if no arguments are provided.  
Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
```
### What are *args and **kwargs?
- `*args` allows you to pass a variable number of non-keyword arguments to a function.
- `**kwargs` allows you to pass a variable number of keyword arguments to a function.

#### Example of *args:
```python
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, 2, 3)  # Output: 1, 2, 3
```

#### Example of **kwargs:
`**kwargs` allows you to pass a variable number of keyword arguments (key-value pairs) to a function. The arguments are accessible as a dictionary inside the function.  
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25
```

In the `**kwargs` example, you can pass any number of named arguments, and they will be received as a dictionary inside the function. 

<!-- ### What are *args and **kwargs?
- `*args` allows you to pass a variable number of non-keyword arguments to a function.
- `**kwargs` allows you to pass a variable number of keyword arguments to a function.  
Example:
```python
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, 2, 3)  # Output: 1, 2, 3
``` -->

### What are lambda functions?
Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.  
Example:
```python
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

### What is recursion?
Recursion occurs when a function calls itself in order to solve a problem. It must have a base case to stop the recursion.  
Example:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Output: 120
```

---

## 📌 Summary
- Functions are reusable blocks of code that perform specific tasks, taking input (parameters) and returning output (values).
- Functions are defined with the `def` keyword and called using the function name with parentheses.
- Parameters allow a function to accept input values, while arguments are the actual values passed during the function call.
- A `return` statement is used to send a result back to the caller.
- Functions can have default parameters, variable arguments (`*args`), and keyword arguments (`**kwargs`).
- Lambda functions provide a concise way to define small, anonymous functions.
- Recursion is when a function calls itself, and it must have a base case to terminate.
