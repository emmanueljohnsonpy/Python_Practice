def outer_func(name):
    def inner_func():
        print(f"Hai {name}")
    return inner_func

res = outer_func("Messi")
res()