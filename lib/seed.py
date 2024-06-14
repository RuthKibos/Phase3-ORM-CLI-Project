#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def seed_database():
    Student.drop_table()
    Course.drop_table()
    Enrollment.drop_table()
    Course.create_table()
    Student.create_table()
    Enrollment.create_table()

    # Create seed data
    computer_science = Course.create("Computer Science", "Engineering", 4)
    literature = Course.create("Literature", "Arts and Humanities", 3)
    physics = Course.create("Physics", "Science", 4)
    psychology = Course.create("Psychology", "Social Sciences", 3)
    statistics = Course.create("Statistics", "Applied_Science", 4)
    economics = Course.create("Economics", "Business", 2)
    nursing = Course.create("Nursing", "Medicine", 5)


    Ruth = Student.create("Ruth", 21, "Ruth@gmail.com")
    Bill = Student.create("Bill", 22, "Bill@gmail.com")
    Brenda = Student.create("Brenda", 20, "Brenda@gmail.com")
    Claire = Student.create("Claire", 19, "Claire@gmail.com")
    Albright = Student.create("Albright", 23, "albright@gmail.com")
    Shifura = Student.create("Shifura", 25, "shifura@gmail.com")
    Ann = Student.create("Ann", 20, "ann@gmail.com")


    # Enroll students in courses
    Enrollment.create(Bill.id, economics.id)
    Enrollment.create(Claire.id, statistics.id)
    Enrollment.create(Ruth.id, computer_science.id)
    Enrollment.create(Bill.id, physics.id)
    Enrollment.create(Brenda.id, literature.id)
    Enrollment.create(Claire.id, psychology.id)
    Enrollment.create(Ruth.id, physics.id)
    Enrollment.create(Brenda.id, computer_science.id)
    Enrollment.create(Albright.id, statistics.id)
    Enrollment.create(Shifura.id, economics.id)
    Enrollment.create(Ann.id, nursing.id)
    Enrollment.create(Albright.id, nursing.id)


seed_database()
print("Seeded database")