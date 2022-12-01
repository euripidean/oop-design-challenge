class Animal:
    def __init__(self, is_endangered = False, offspring_num = 0):
        """Animal class for zoo"""
        self.is_endangered = is_endangered
        self.offspring_num = offspring_num
        self.inventory = []

    def add_to_endangered(self):
        self.is_endangered = True
        print(f"Oh noes! The {self.species} is now endangered.")

    def pregnant(self):
        if self.gender == 'F':
            self.offspring_num += 1
            self.is_endangered = False
            print(f"Great news! The {self.species} is pregnant.\n Conservation efforts successful.")
        else:
            print(f"Steady on! This isn't possible...yet.")

    def eat(self):
        print("The animal eats.")

    def add_to_inventory(self, animal):
        self.inventory.append(animal)
        print(f'{animal.name} added to Zoo registry')
