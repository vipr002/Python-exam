# question 2
# a)
class Student:
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return "name:" + str(self.name) + "mark:" + str(self.mark)

    # b)
    def passOrFail(self):
        if self.mark >= self.passingMark:
            return "Pass"
        else:
            return "Fail"


# c)
student1 = Student("John", 52)

status1 = student1.passOrFail()
print(status1)

# d)
student2 = Student("Jenny", 69)

status2 = student2.passOrFail()
print(status2)

# updating passingMark to 60
Student.passingMark = 60

status1 = student1.passOrFail()
print(status1)

status1 = student2.passOrFail()
print(status2)
