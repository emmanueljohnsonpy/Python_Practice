

nested_list = [[1, [2, 3]], [4, 5], [6, [7, [8]]]]
def flatten_list(nested_list):
    res = []
    for i in nested_list:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res

print(flatten_list(nested_list))