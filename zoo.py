class Zoo:
    def __init__(self, name, location, opening_hours, employees = []):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours
        #Employees is a private attribute so no one can access employee data.
        self.employees = employees

    def show_hours(self):
        print(f"The opening hours for {self.name} are: {self.opening_hours}.")

    def add_employee(self, employee):
        self.employees.append(employee)
        
