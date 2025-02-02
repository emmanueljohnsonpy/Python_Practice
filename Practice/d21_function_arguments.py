""" 
def average(a=3,b=1):
    print("Average is ",(a+b)/2)

average(a=9)
"""

# Arbitrary argument
""" 
def average(*numbers):
    print(type(numbers))
    sum1=0
    for i in numbers:
        sum1=sum1+i
    print(sum1/len(numbers))
    
average(10,20,30) 
"""

# Keyword arbitrary argument

def name(**name):
    print(type(name))
    print("hai", name["fname"], name["lname"])

name(lname="Johnson", fname="Emmanuel")
