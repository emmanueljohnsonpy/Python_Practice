""" a=input("Enter the number : ")
print(f"Multiplication table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{i} x {a} = {(int(a)*int(i))}")
# except Exception as e:
#     print(e)
except:
    print("Invalid Input")

print("Some code is here") """

try:
    num=int(input("enter a integer : "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("enter integer")
except IndexError:
    print("enter 0 or 1")
    