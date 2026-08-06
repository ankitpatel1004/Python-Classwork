from faker import Faker
fake = Faker()
import random
from myapp.models import *

def create(n=50):
    depts = Dept.objects.all()
    for i in range(n):
        name = fake.name()
        email = fake.email()
        age = random.randint(21,30)
        dept = depts[random.randint(0,len(depts)-1)]
        enno = Enrollment.objects.create(en_no=f"STD_{random.randint(100,999)}")

        Student.objects.create(name=name,email=email,age=age,dept=dept,en_no=enno)
        print("Done..")

def result():
    students = Student.objects.all()
    subjects = Subject.objects.all()
    for student in students:
        for subject in subjects:
            Marks.objects.create(student=student,suuject=subject,marks=random.randint(1,100))
