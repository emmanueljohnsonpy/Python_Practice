""" i=0
while i<3:
    print(i)
    i=i+1
print("done") """

""" i=int(input("enter"))
while(i<=10):
    i=int(input("enter"))
    print(i)

print("done") """

""" count=5
while count>0:
    print(count)
    count-=1
else:
    print("out of while") """

""" for i in range(6):
    print(i)
    if i==3:
        break
else:
    print("out of for loop") """

# do while loop emulate
""" i=0
while True:
    print(i)
    i+=1
    if i<5:
        continue
    else:
        break """

i=0
while True:
    print(i)
    i+=1
    if i%100==0:
        break