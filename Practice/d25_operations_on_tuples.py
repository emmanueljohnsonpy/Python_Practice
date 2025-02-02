""" countries = ("Spain","Italy","India")
temp=list(countries)
temp.append("France")
countries=tuple(temp)
print(countries) """

""" a=(1,2,3,4,5)
b=(6,7,8,9)
c=a+b
print(c) """

a=(1,1,1,1,2,3,4,5)
res=a.count(1)
print(res)
print(a.index(3))
print(a.index(4,5,8))