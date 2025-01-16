""" marks=[1,7,2,3,7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[-3])

if 7 in marks:
    print("Yes")
else:
    print("No")

if "ha" in "aha":
    print("True")

print(marks[1:5:3]) """

# List comprehension

lst=[i*i for i in range(7) if i%2==0]
print(lst)