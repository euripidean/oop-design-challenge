from animal import Animal

class Turtle(Animal):
    def __init__(self, name, age, gender, species='Turtle'):
        """Initialise turtle class"""
        super().__init__(is_endangered = False, offspring_num = 0)
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
       
    def swim(self):
        """Turtles swim"""
        print(f"{self.name} is swimming!")

    def eat(self):
        """Turtles eat method"""
        print(f"Mmm eating all of this lettuce is delicious!")


