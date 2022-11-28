class Animal:
    def __init__(self, species, gender, is_endangered = False, offspring_num = 0):
        self.species = species
        self.gender = gender
        self.is_endangered = is_endangered
        self.offspring_num = offspring_num

    def add_to_endangered(self):
        self.is_endangered = True
        print(f"Oh noes! The {self.species} is now endangered.")

    def pregnant(self):
        if self.gender == 'F':
            offspring_num += 1
            self.is_endangered = False
            print(f"Great news! The {self.species} is pregnant.\n Conservation efforts successful.")
