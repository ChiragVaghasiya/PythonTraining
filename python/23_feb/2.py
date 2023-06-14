# 2.Define a class Person with the following attributes: name, age, address. The class should have a method introduce that returns a string introducing the person in the following format: "Hi, my name is [Name] and I am [Age] years old. I live in [Address]."
#     • Output: Hi, my name is John Doe and I am 30 years old. I live in 123 Main Street.

# 3.Define a class Student that inherits from the Person class. The Student class should have an additional attribute student_id and a method enroll that returns a string in the following format: "Hi, my name is [Name] and I am a student with ID [Student ID]."
#     • Output: Hi, my name is Jane Doe and I am 20 years old. I live in 456 Market Street.
#     • Output: Hi, my name is Jane Doe and I am a student with ID 12345.


class Person:

    def __init__(self) -> None:
        self.name = input("Enter Your Name")
        self.age = int(input("Enter Your Age"))
        self.address =  input("Enter Your Address")

    def func1(self):
        return f'Hi, my name is {self.name} and I am {self.age} years old. I live in {self.address}'

class Student(Person):

    def __init__(self) -> None:
        Person.__init__(self)
        self.student_id = int(input("Enter Your Student Id"))

    def func2(self):
        return f'Hi, my name is {self.name} and I am a student with ID {self.student_id}'

# person1 = Person()
person1 = Student()

print(person1.func1())
print(person1.func2())