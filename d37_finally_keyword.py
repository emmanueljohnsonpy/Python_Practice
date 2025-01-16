def func1():
    try:
        l=[1,4,5,3]
        i=int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("I always executed")

x=func1()
print(x)