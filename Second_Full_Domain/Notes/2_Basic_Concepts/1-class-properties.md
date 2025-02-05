
### **Class Properties in Python**

In Python, **class properties** are attributes that belong to a class rather than an instance of the class. They are typically defined using the `@property` decorator and are useful when you want to control access to class attributes.

---

### **Types of Class Properties**
1. **Instance Properties** (Defined inside `__init__`)
2. **Class Properties** (Defined at the class level using `@classmethod` or `@property`)

---

### **1. Using `@property` (Instance-Level)**
The `@property` decorator allows you to define **getter, setter, and deleter** for an instance attribute.

#### **Example**
```python
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):  # Getter
        return self._price

    @price.setter
    def price(self, value):  # Setter
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):  # Deleter
        print("Deleting price...")
        del self._price

# Usage
p = Product(100)
print(p.price)  # Calls getter
p.price = 150   # Calls setter
del p.price     # Calls deleter
```
💡 **Advantage**: Controls access and validation of attributes.

---

### **2. Using `@classmethod` (Class-Level)**
Class properties operate at the **class level** rather than at the instance level. We use `@classmethod` along with `@property` to create a class property.

#### **Example**
```python
class Product:
    _tax = 0.05  # Class attribute

    @classmethod
    @property
    def tax(cls):
        return cls._tax

    @classmethod
    def set_tax(cls, value):
        if value < 0:
            raise ValueError("Tax cannot be negative!")
        cls._tax = value

# Usage
print(Product.tax)  # Calls getter
Product.set_tax(0.08)
print(Product.tax)  # Updated tax
```
💡 **Advantage**: Allows control over **class-level attributes** without needing an instance.

---

### **When to Use Class Properties?**
- When you need **read-only attributes**.
- When you want **automatic validation** before setting values.
- When managing **class-level data** with controlled access.