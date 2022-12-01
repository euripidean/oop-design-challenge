# oop-design-challenge

## The Project
For the OOP Design Challenge, we decided to create objects around the idea of a Zoo: an establishment with lots of varieties when it comes to departments and interactivity.

We created a class for the Zoo itself which contains a list of employees composited from the Employee class. Employees also have the Zoo class featured as their employer.

Zoo methods include adding an employee to the list of employees and advertising the opening hours of the Zoo. We see this as a mainly administrative class.

Each instance of the Employee class type can introduce themselves to a client with the introduce() method. We can also regenerate their employee id, although this method would be best off being private for future developers as we don't want just anyone to be able to do that.

For the inhabitants of the Zoo, we have an overarching Animal class which is key for the conservation efforts of the Zoo.

Methods on the Animal class include tracking the number of offspring an animal has and also whether that animal type is endangered.

Inheriting from Animal we have Lion and Turtle, two examples of how broad the animal class can be.
Lion methods override the default animal methods: assuming lions always have two cubs, we change the offspring_num update for Lions who have the pregnant() method called. Similarly, Lions eat a very different diet from Turtles, so this is reflected in the eat() method.

## UML Diagram
![alt text](https://github.com/euripidean/oop-design-challenge/blob/main/uml.jpg?raw=true)







## Video Walk-through
Click the following URL to watch a video walk-through of our program on YouTube!
https://www.youtube.com/watch?v=QiSGGVVfdns
