class Employee:  # parent class
    empCount = 0
    tsal = 0
    avgsal = 0
    def __init__(self, name, family, salary, department):  # all parameters
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.tsal += int(salary)

    def average_salary(self):
        print("average salary of %d" % (Employee.tsal / Employee.empCount))

    def explain_interitance(self):
        print("this is output from parent class")

    def print_emp(self):
        print("Employee name:", self.name)
        print("Family:",self.family)
        print("salary:",self.salary)
        print("department:",self.department)
class Fulltime_Employee(Employee):
    def another_method(self):
        print("this is outpur from child class")
emp1 = Employee("Anusha", "Palla ", "1000", "CS")
emp2 = Employee("Prakash", "Ravella", "2000", "EE")
emp3 = Employee("Raji", "cholleti", "2500", "CS")
emp4 = Employee("ANU", "gaddam", "3000", "CS")
emp5 = Fulltime_Employee("Anush", "reddy", "5000", "CS")
print("Total Employee %d" % Employee.empCount)
print("average salary of %d" % (Employee.tsal / Employee.empCount))

emp4.average_salary()

print("first employee")
emp1.print_emp()
emp2.print_emp()
emp2.print_emp()
emp4.print_emp()
emp5.explain_interitance()
emp5.another_method()
