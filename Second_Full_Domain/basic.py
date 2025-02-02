""" num = 1
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

print(check_prime(num)) """


# my_tuple = (1, 2)
# new_tuple = (3, 4)
# my_tuple += new_tuple
# print(my_tuple)

""" 
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
except NegativeNumberError as e:
    print(e)
 """
""" multiply = lambda x, y: x * y
print(multiply(3, 5)) """

""" numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** 2, numbers)) 
print(square) """

""" from functools import reduce

def factorial(num):
    nums = [i for i in range(1, num + 1)]
    result = reduce(lambda x, y: x * y, nums)
    return result

print(factorial(5)) """

""" s = "*"
print(s.isalnum())
 """









print("yo")
# total = lambda x, y: x + y
# print(total(10, 5))

""" from functools import reduce

num = 5
nums = [i for i in range(1, num + 1)]
result = reduce(lambda x, y: x * y, nums)
print(result) """




my_dict = {
    "name": "Ronaldo",
    "team": "Portugal",
    7: True,
    "other_teams": ["al nasar", "real madrid", "Juventus"],
    "again": {
        "name" : "ronaldo",
        "team": "Porutgal",
    }
}
my_list = []
for i,j in my_dict.items():
    if type(j) == str:
        print(i,j)
    else:
        my_list.append(i)

for i in my_list:
    del my_dict[i]

print(my_dict)