# second largest even number


nums = [1, 2, 3, 4, 5, 6, 7]
second = 0
first = 0
for i in nums:
    if i % 2 == 0:
        if i > first:
            second = first
            first = i
        if i < first and i > second:
            second = i
print(second)
