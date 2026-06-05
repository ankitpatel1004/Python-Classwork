class Hod:
    def role(self):
        print("Head of the department - Management")
class Teacher(Hod):
    def skill(self):
        print("Teacher - Teaching")
class Student(Teacher):
    def work(self):
        print("Student - Study")
s = Student()
s.role()
s.skill()
s.work()
