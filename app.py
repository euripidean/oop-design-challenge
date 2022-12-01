from zoo import Zoo
from employees import Employees
from lion import Lion
from turtle import Turtle

#Create versions of each class

the_best_zoo = Zoo('Best Zoo Ever', 'Loveland', '9 to 5')

#Zoo methods:
the_best_zoo.show_hours()

#Create employees
employee_1 = Employees(the_best_zoo,'Alexa Whitney', 35, 13)
employee_2 = Employees(the_best_zoo,'Jane Harrison', 38, 2)

#Run employee methods

#Add employees to list of Zoo Employees
the_best_zoo.add_employee(employee_1)
the_best_zoo.add_employee(employee_2)

#Confirm employees are in list
for item in the_best_zoo.employees:
    print(item.name)

#Employee methods:
employee_1.introduce()
employee_2.introduce()
employee_2.update_id()

# Create lions
nala = Lion('Nala', 6, 'F')
simba = Lion('Simba',5,'M')

#Run and test lion methods
nala.add_to_endangered()
#check this has been updated
print(nala.is_endangered)
simba.eat()
nala.eat()

# Create turtles
squirtle = Turtle('Squirtle', 55, 'F')
crush = Turtle('Crush', 2, 'M' )

#Run and test turtle and other methods
crush.add_to_endangered()
crush.pregnant()
squirtle.swim()
squirtle.pregnant()
squirtle.eat()

