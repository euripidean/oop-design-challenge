class Zoo:
    def __init__(self, name, location, opening_hours, employees = []):
        """Initialise Zoo"""
        self.name = name
        self.location = location
        self.opening_hours = opening_hours
        #Employees is a private attribute so no one can access employee data.
        self.employees = employees
        self.enclosure = []

    def show_hours(self):
        """Prints opening hours of zoo"""
        print(f"The opening hours for {self.name} are: {self.opening_hours}.")

    def add_employee(self, employee):
        """Adds employee to list"""
        self.employees.append(employee)

    def add_to_enclosure(self, animal):
        """Adds animals to enclosure"""
        self.enclosure.append(animal)
        
