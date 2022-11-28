from zoo import Zoo
from animal import Animal
from employees import Employees
from lion import Lion
from turtle import Turtle

#Create versions of each class

the_best_zoo = Zoo('Best Zoo Ever', 'Loveland', '9 to 5')

#Create employees
employee_1 = ('Alexa Whitney', 35, 13)
employee_2 = ('Jane Harrison', 38, 2)

the_best_zoo.add_employee(employee_1)
the_best_zoo.add_employee(employee_2)

lions = Animal('Lion', 'F')
simba = Lion('Simba','F', 6)
