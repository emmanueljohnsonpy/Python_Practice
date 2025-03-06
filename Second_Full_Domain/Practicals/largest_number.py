# second largest even number


nums = [10, 8, 12, 14, 16]
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
