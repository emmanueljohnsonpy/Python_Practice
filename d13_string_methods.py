# Strings are immutable
a="!!!!!!! !!Harry!!!!!! !!!!Harry!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "Emmanuel"))
print(a.split())
blogheading="introduction to pyThon"
print(blogheading.capitalize())
print(blogheading.center(50))
print(a.count("Harry"))
print(a.endswith("."))
print(a.endswith("Harry",10,15))
print(a.find("Harr")) # return -1
print(a.index("H")) # return error , find and index same like working
str1="Welc00om\ne"
print(str1.isalnum())
print(str1.isalpha())
print(str1.islower())
print(str1.isprintable())
str1="  "
print(str1.isspace())
str1="World Health organization"
print(str1.istitle())
print(str1.isupper())
print(str1.startswith("World"))
print(str1.swapcase())
print(str1.title())