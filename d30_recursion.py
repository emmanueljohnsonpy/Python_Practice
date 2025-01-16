def rec(x):
    if x==1:
        return 1
    return x*rec(x-1)

print(rec(5))