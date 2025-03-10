
def my_func(*args, **kwargs):
    if "Err" in kwargs:
        raise ValueError("Don't enter Err as key")
    print("NO Error")

try:
    my_func(10, 20, 30, Argentina = "messi", Err = "ronaldo")
except ValueError as e:
    print(e)
