# string

""" string="Harry"
res=len(string)
print(res)
res=string.endswith("rry")
print(res)
res=string.count("r")
print(res)
res=string.capitalize()
print(res)
res=string.find("r")
print(res)
res=string.replace("r", "a")
print(res) """

""" l1=[1,8,7,2,21,15]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(8)
print(l1)
l1.insert(3,200)
print(l1)
l1.pop(3)
print(l1)
l1.remove(8)
print(l1) """

""" l1=(1,8,7,2,21,15)
res=l1.count(7)
print(res)
res=l1.index(1)
print(res) """

""" a={"name": "Harry",
   "from": "India",
   "marks": [92,98,96]}
res=a.items()
print(res)
res=a.keys()
print(res)
res=a.values()
print(res)
a.update({"friend": "Sam"})
print(a)
a["friend2"]= "Jenny"
print(a)
res=a.get("name")
print(res) """

""" a={1,2,3,4,5}
b={3,4,5,6,7}
s={1,8,2,3}
res=len(s)
print(res)
s.remove(8)
print(s)
res=s.pop()
print(res)
s.clear()
print(s)
res=a.union(b)
print(res)
res=a.intersection(b)
print(res) """



""" a=[1,2,3,4,5,6]
l1=0
l2=0
for i in a:
   if i>l1:
        l2=l1
        l1=i
   if i>l2 and i<l1:
       l2=i
print(l2) """

a=[1,2,3,4,5,6]
i=0
while i<len(a)//2:
   a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i] 
   i+=1
print(a)

   