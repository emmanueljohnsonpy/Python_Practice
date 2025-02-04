# Lists in Python (Cornell Method)

## 📌 Cue Column (Keywords/Questions) | 📌 Notes Column (Detailed Explanation)

### What is a list?
A list is a collection of ordered, mutable elements. Lists can store items of different data types.  
Example:  
```python
my_list = [1, 2, 3, "apple", 4.5]
```

### Properties of Lists
- **Ordered**: The items in a list are arranged in a specific order, and the order is maintained. Each item can be accessed by its position or index (starting from 0).
- **Mutable**: The elements in a list can be changed after the list is created. You can modify, add, or remove items.
- **Different Data Types**: A list can hold elements of various types, like integers, strings, floats, or even other lists. 

### How to create a list?
A list is created by placing elements inside square brackets, separated by commas.  
Example:  
```python
my_list = [1, 2, 3, "apple"]
```

### How to access elements in a list?
Use the index of the element (starting from 0) to access items.  
Example:  
```python
my_list = [1, 2, 3, "apple"]
print(my_list[0])  # Output: 1
```

### How to modify elements in a list?
You can modify list elements by assigning new values to a specific index.  
Example:  
```python
my_list = [1, 2, 3]
my_list[1] = 5
print(my_list)  # Output: [1, 5, 3]
```

### What are list methods?
Lists have various built-in methods, such as:
- `.append()` – Adds an item to the end of the list.
- `.remove()` – Removes the first occurrence of a specified value.
- `.pop()` – Removes and returns the item at the specified index.
- `.extend()` – Adds all elements of an iterable to the list.

Example:  
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

### How to slice a list?
You can slice a list to get a part of it. The syntax is `list[start:end]`.  
Example:  
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4]
```

### What are nested lists?
A nested list is a list inside another list.  
Example:  
```python
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2]
```

### How to iterate over a list?
You can use a `for` loop to iterate over the elements of a list.  
Example:  
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
```

---

## 📌 Summary
- Lists are ordered and mutable collections that can store mixed data types.
- The order of items in a list is maintained, and elements can be accessed via their index.
- Lists can hold items of different data types, such as integers, strings, or even other lists.
- Lists have built-in methods like `.append()`, `.remove()`, and `.pop()`.
- You can slice lists and create nested lists for more complex data structures.
