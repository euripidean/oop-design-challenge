from random import randint

def random_employee_id(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class Employees:
    def __init__(self, employer, name, age, years_of_service = 0):
        """Initialise employee"""
        self.employer = employer
        self.name = name
        self.age = age
        self.years_of_service = years_of_service

        self.employee_id = random_employee_id(8)

    def introduce(self):
        print(f"Hi! My name is {self.name} and I have worked at {self.employer.name} for {self.years_of_service} years. How can I help you?")

    def update_id(self):
        print(f"I quit and came back. My new employee id is {self.employee_id}.")
