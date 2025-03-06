

# Dictionary longest string ulla value nta key value delete cheyan dictionary ne

my_dict = {"key1": "mango", "key2": "apple", "key3": "orange"}
k = None
v = 0
for key, value in my_dict.items():
    if len(value) > v:
        v = len(value)
        k = key
del my_dict[k]
print(my_dict)