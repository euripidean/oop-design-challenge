from animal import Animal

class Turtle(Animal):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def swim(self):
        print(f"{self.name} is swimming!")

    def eat(self):
        print(f"Mmm eating all of this lettuce is delicious!")

