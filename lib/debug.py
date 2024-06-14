#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
import ipdb


def reset_database():
    Enrollment.drop_table()
    Course.drop_table()
    Student.drop_table()
    Student.create_table()
    Course.create_table()
    Enrollment.create_table()

    # Create seed data
    computer_science = Course.create("Computer Science", "Engineering", 4)
    literature = Course.create("Literature", "Arts and Humanities", 3)
    physics = Course.create("Physics", "Science", 4)
    psychology = Course.create("Psychology", "Social Sciences", 3)
    statistics = Course.create("Statistics", "Applied Science", 4)
    economics = Course.create("Economics", "Business", 2)
    nursing = Course.create("Nursing", "Medicine", 5)

    Ruth = Student.create("Ruth", 21, "ruth@gmail.com")
    Bill = Student.create("Bill", 22, "bill@gmail.com")
    Brenda = Student.create("Brenda", 20, "brenda@gmail.com")
    Claire = Student.create("Claire", 19, "claire@gmail.com")
    Albright = Student.create("Albright", 23, "albright@gmail.com")
    Shifura = Student.create("Shifura", 23, "shifura@gmail.com")
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
    
reset_database()
ipdb.set_trace()