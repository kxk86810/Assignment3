
class Employee:
    count = 0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
    def averageSalary(self):
        average = self.salary / Employee.count
        return average

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

a1 = Employee("John", "Smith", 48000, "IT")
a2 = Employee("David", "Jones", 45000, "HR")
a3 = FulltimeEmployee("Sam", "Williams", 60000, "Marketing")

print(a1.averageSalary())
print(a2.averageSalary())
print(a3.averageSalary())