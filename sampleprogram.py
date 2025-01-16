""" def facto(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res

res=facto(5)
print(res) """

""" for i in range(1,6):
    n=6-i
    for j in range(1,6):
        if j<=6-i:
            print(f"{n}",end="")
        n-=1
    print() """

""" mydict={
    'name': 'John',
    'place': 'Ekm',
    'course': 'Python'
}

print(mydict)
mydict['fees']=200
print(mydict)
mydict.pop('fees')
print(mydict)

for k in mydict.keys():
    print(k) """

""" list1=['apple', 'orange', 'grapes']
list2=['banana', 'orange', 'lemon']
res=list1+list2
remove_duplicates=set(res)
print(remove_duplicates) """
