from animal import Animal

class Lion(Animal):
    def __init__(self, name, age, gender, species='Lion'):
        """Initialise Lion instances"""
        super().__init__(is_endangered = False, offspring_num = 0)
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        

    def eat(self):
        """Lion specific eat method"""
        print(f"{self.name} just ate a delicious meal of gazelle!")

    def pregnant(self):
        """Lions always have two cubs so updating pregnancy method"""
        super().pregnant()
        self.offspring_num += 2
        print(f"Congratulations! {self.name} is expecting 2 cubs!")
