from animal import Animal

class Lion(Animal):
    def __init__(self, name, age, gender, species='Lion'):
        super().__init__(is_endangered = False, offspring_num = 0)
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        

    def eat(self):
        print(f"{self.name} just ate a delicious meal of gazelle!")

    def pregnant(self):
        super().pregnant()
        self.offspring_num += 2
        print(f"Congratulations! {self.name} is expecting 2 cubs!")


nala = Lion('Nala', 6, 'F')
# print(help(nala))
print(nala.age)
nala.add_to_endangered()
print(nala.is_endangered)
