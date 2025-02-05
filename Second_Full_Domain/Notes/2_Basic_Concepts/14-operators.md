# Operators in Python (Cornell Method)

## Questions & Key Points
1. **What are operators in Python?**
2. **What are the different types of operators?**
3. **How do arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators work?**
4. **What are unary, binary, and ternary operators?**
5. **When should each type of operator be used?**

---

## Notes

### 1. What are Operators?
Operators are special symbols in Python that perform operations on variables and values.

### 2. Types of Operators
Python has several types of operators:

#### a) Unary Operators
Unary operators operate on a single operand.

| Operator | Description | Example |
|----------|-------------|----------|
| `+` | Unary positive | `+a` |
| `-` | Unary negative | `-a` |
| `~` | Bitwise NOT | `~a` |
| `not` | Logical NOT | `not a` |

#### b) Binary Operators
Binary operators operate on two operands.

| Operator | Description | Example |
|----------|-------------|----------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `and` | Logical AND | `a and b` |
| `or` | Logical OR | `a or b` |

#### c) Ternary Operators (Conditional Expression)
Ternary operators work with three operands and are used for conditional expressions.

| Operator | Description | Example |
|----------|-------------|----------|
| `condition ? true_value : false_value` | Returns `true_value` if condition is true, else `false_value` | `x = 10 if a > b else 20` |

#### d) Arithmetic Operators
Used to perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|----------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `//` | Floor Division | `a // b` |
| `%` | Modulus | `a % b` |
| `**` | Exponentiation | `a ** b` |

#### e) Comparison Operators
Used to compare two values.

| Operator | Description | Example |
|----------|-------------|----------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

#### f) Logical Operators
Used to combine conditional statements.

| Operator | Description | Example |
|----------|-------------|----------|
| `and` | Returns True if both statements are true | `a > 3 and b < 10` |
| `or` | Returns True if one of the statements is true | `a > 3 or b < 10` |
| `not` | Reverses the result | `not(a > 3)` |

#### g) Bitwise Operators
Used to perform bit-level operations.

| Operator | Description | Example |
|----------|-------------|----------|
| `&` | AND | `a & b` |
| `|` | OR | `a | b` |
| `^` | XOR | `a ^ b` |
| `~` | NOT | `~a` |
| `<<` | Left shift | `a << 2` |
| `>>` | Right shift | `a >> 2` |

#### h) Assignment Operators
Used to assign values to variables.

| Operator | Description | Example |
|----------|-------------|----------|
| `=` | Assign | `a = 5` |
| `+=` | Add and assign | `a += 5` |
| `-=` | Subtract and assign | `a -= 5` |
| `*=` | Multiply and assign | `a *= 5` |
| `/=` | Divide and assign | `a /= 5` |
| `//=` | Floor divide and assign | `a //= 5` |
| `%=` | Modulus and assign | `a %= 5` |
| `**=` | Exponentiate and assign | `a **= 5` |

#### i) Identity Operators
Used to compare object identity.

| Operator | Description | Example |
|----------|-------------|----------|
| `is` | Returns True if both variables are the same object | `a is b` |
| `is not` | Returns True if both variables are not the same object | `a is not b` |

#### j) Membership Operators
Used to check if a value exists in a sequence.

| Operator | Description | Example |
|----------|-------------|----------|
| `in` | Returns True if a value is present in the sequence | `5 in [1, 2, 3, 5]` |
| `not in` | Returns True if a value is not present in the sequence | `6 not in [1, 2, 3, 5]` |

---

## Summary
- **Unary operators** operate on a single operand.
- **Binary operators** operate on two operands.
- **Ternary operators** use three operands for conditional expressions.
- **Arithmetic operators** perform basic mathematical operations.
- **Comparison operators** compare values and return boolean results.
- **Logical operators** help in combining multiple conditions.
- **Bitwise operators** perform operations at the binary level.
- **Assignment operators** modify and assign values to variables.
- **Identity operators** check object identity.
- **Membership operators** check for value presence in a sequence.
- Understanding these operators helps in writing efficient and readable Python code.

