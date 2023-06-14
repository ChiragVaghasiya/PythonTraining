import re
class Employee:
    no_of_leaves = 10       #creating templates
    object_count = 0
    def func1(self):
        return f"Emloyee name is {self.name} , salarrry is {self.sallary} and that employee role is {self.role}"

    def __init__(self , fname , frole , fsallary) -> None:
        Employee.object_count += 1 
        self.name = fname
        self.role = frole
        self.sallary = fsallary
    
    @classmethod
    def objectee_count(cls,x):
        cls.object_count = x
        return f'Total objects is {cls.object_count} of the {cls.__name__}'

    @classmethod
    def conVertation(cls,string):
        params = re.split(r'-|,| ',string)
        print(params)
        return cls(params[0],params[1],params[2])

# creating objects --in this emp1 &emp2
# emp1 = Employee("daku","Devloper",6000)
# emp2 = Employee("sk","HR",2500)
emp3 = Employee.conVertation("ketan-jr.Devloper-9000")

# print(Employee.__dict__)
# print(emp1.__dict__)
# print(emp2.__dict__)
print(emp3.__dict__)

# emp1.no_of_leaves = 12
# Employee.no_of_leaves  = 9
# print(Employee.no_of_leaves)
# print(emp1.no_of_leaves)

# print(emp1.func1())
# print(emp2.func1())

# print(Employee.objectee_count(500))
