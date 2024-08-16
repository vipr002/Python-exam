# question 1

# parent class Person
class Person:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


# child class Student, inherits from Person class
class Student(Person):
    def __init__(self, fname, lname, age, studentid):
        super().__init__(fname, lname, age)
        self.student_id = studentid

    def get_stuinfo(self):
        super().get_info()
        print("Student ID:", self.student_id)


# child class Employee, inherits from Person class
class Employee(Person):
    def __init__(self, fname, lname, age, employeenum, salary):
        super().__init__(fname, lname, age)
        self.employeenum = employeenum
        self.salary = salary

    def get_empinfo(self):
        super().get_info()
        print("Employee No:", self.employeenum)
        print("Salary:", self.salary, "USD")


# test
new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()

print("==========================")

new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
new_employee.get_empinfo()