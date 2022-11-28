from animal import Animal

class Lion(Animal):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        print(f"{self.name} just ate a delicious meal of gazelle!")

    def pregnant(self):
        super().pregnant()
        self.offspring_num += 2
        print(f"Congratulations! {self.name} is expecting 2 cubs!")
