def fact(x):
    if x == 1:
        return x
    return x*fact(x-1)

print(fact(3))

