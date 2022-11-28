from random import randint

def random_employee_id(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class Employees:
    def __init__(self, name, age, years_of_service = 0):
        self.name = name
        self.age = age
        self.years_of_service = years_of_service

        employee_id = random_employee_id(8)
