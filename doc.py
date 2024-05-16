"""class Professor:
    # Class attribute
    Name = "Anas"

    # Constructor method
    def __init__(self, name, teaches):
        self.Name = name
        self.Teaches = teaches
        #print(f"Professor {self.Name} teaches {self.Teaches}")

    # Class method
    def grade(self, assignment):
        print(f"{self.Name} is grading a {self.Teaches} {assignment}.")

# Creating objects of the Professor class
professor1 = Professor("Anas", "OOP")
professor2 = Professor("Mossab", "HCI")

# Calling the grade method
professor1.grade("project")
professor2.grade("assignment")"""

# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Child class inheriting from Person
class Professor(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent's constructor
        self.subject = subject

    # Method overriding
    def greet(self):
        print(f"Hello, I am Professor {self.name}, and I teach {self.subject}.")

# Creating objects
person = Person("Anas")
professor = Professor("Raja", "Computer Networks")

# Calling the greet() method
person.greet()  # Output: Hello, my name is John.
professor.greet()  # Output: Hello, I am Professor Jane, and I teach Computer Science.
