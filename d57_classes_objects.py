class Person:
    # name = "Ronaldo"
    # team = "Portugal"

    def info(self):
        print(f"{self.name} in {self.team}")

obj1=Person()
obj2=Person()
obj1.name="Messi"
obj1.team="Argentina"
obj2.name="Neymar"
obj2.team="Brazil"
obj1.info()
obj2.info()

