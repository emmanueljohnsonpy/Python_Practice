x=90
match x:
    case 0:
        print("its zero")
    case 1:
        print("it is one")
    case _ if x!=90:
        print("is not 90")
    case _ if x<100:
        print("is not 70")
    case _:
        print(x)