name = "my name is emmanuel"
print(" ".join([i.replace(i[0], i[0].upper(), 1) for i in name.split()]))