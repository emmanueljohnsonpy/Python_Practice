dic = {
    "Harry":"deadly professional",
    "role":"ml and ai"
}

# print(dic["Harry"])
# print(dic.get("Harry"))

# print(dic.keys())
# for i in dic.keys():
#     print(i)

# for i in dic.keys():
#     print(f"The value corresponding to the key {i} is {dic[i]}")


for key, value in dic.items():
    print(f"{key} is {value}")