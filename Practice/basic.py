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


class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
except NegativeNumberError as e:
    print(e)
