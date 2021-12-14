class Zoo:
    def __init__(self, animal1, animal2, animal3):
        self.animal1 = animal1
        self.animal2 = animal2
        self.animal3 = animal3
        self.animal4 = [animal2, animal3]

z = Zoo("Tigr", "Begemot", "Jiraf")

print(z.animal1, z.animal2, z.animal3)
z.animal1 = 'lion'
z.animal3 = 'snake'
print(z.animal1, z.animal2, z.animal3, z.animal4)
