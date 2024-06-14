from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def exit_program():
    print("Thank you for interacting with our PLatform")
    exit()

#student functions
def list_students():
    students = Student.get_all()
    for student in students:
        print(student)

def find_student_by_name():
    name = input("Enter the student's name: ")
    student = Student.find_by_name(name)
    print(student) if student else print(
        f'Student {name} not found')

def find_student_by_id():
    id_ = input("Enter the student's id: ")
    student = Student.find_by_id(id_)
    print(student) if student else print(f'Student {id_} not found')

def find_student_by_age():
    age = input("Enter the student's age: ")
    student = Student.find_by_age(age)
    print(student) if student else print(f'Student {age} not found')

def create_student():
    name = input("Enter the Student's name: ")
    age = input("Enter the Student's age: ")
    email = input("Enter the Student's email: ")
    try:
        age = int(age)
        student = Student.create(name, age, email)
        print(f'Success: {student}')
    except Exception as exc:
        print("Error creating student: ", exc)

def update_student():
    """Update an existing student."""
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        try:
            name = input("Enter the student's new name: ")
            student.name = name
            age = input("Enter the student's new age: ")
            student.age = int(age)
            email = input("Enter the student's new email: ")
            student.email = email

            student.update()
            print(f'Success: {student}')
        except Exception as exc:
            print("Error updating student: ", exc)
    else:
        print(f'Student {id_} not found')

def delete_student():
    """Delete an existing student."""
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        student.delete()
        print(f'Student {id_} deleted')
    else:
        print(f'Student {id_} not found')

    
#Course functions
#List all courses.
def list_courses():
    courses = Course.get_all()
    for course in courses:
        print(course)

#Find a course by name.
def find_course_by_name():
    name = input("Enter the course's name: ")
    course = Course.find_by_name(name)
    print(course) if course else print(f'Course {name} not found')

#Find a course by ID.
def find_course_by_id():
    id_ = input("Enter the course's id: ")
    course = Course.find_by_id(id_)
    print(course) if course else print(f'Course {id_} not found')

 #Create a new course.
def create_course():
    name = input("Enter the course's name: ")
    department = input("Enter the course's department: ")
    credits = int(input("Enter the course's credits: "))
    try:
        course = Course.create(name, department, credits)
        print(f'Success: {course}')
    except Exception as exc:
        print("Error creating course: ", exc)

#Update an existing course.
def update_course():
    id_ = input("Enter the course's id: ")
    if course := Course.find_by_id(id_):
        try:
            name = input("Enter the course's new name: ")
            course.name = name
            department = input("Enter the course's new department: ")
            course.department = department
            credits = int(input("Enter the course's new credits: "))
            course.credits = credits

            course.update()
            print(f'Success: {course}')
        except Exception as exc:
            print("Error updating course: ", exc)
    else:
        print(f'Course {id_} not found')

#Delete an existing course.
def delete_course():
    id_ = input("Enter the course's id: ")
    if course := Course.find_by_id(id_):
        course.delete()
        print(f'Course {id_} deleted')
    else:
        print(f'Course {id_} not found')

#Enrollment functions
#List all enrollments.
def list_enrollments():
    enrollments = Enrollment.get_all()
    for enrollment in enrollments:
        print(enrollment)

 #Find an enrollment by ID.
def find_enrollment_by_id():
    id_ = input("Enter the enrollment's id: ")
    enrollment = Enrollment.find_by_id(id_)
    print(enrollment) if enrollment else print(f'Enrollment {id_} not found')

#Create a new enrollment.
def create_enrollment():
    student_id = int(input("Enter the student's id: "))
    course_id = int(input("Enter the course's id: "))
    try:
        enrollment = Enrollment.create(student_id, course_id)
        print(f'Success: {enrollment}')
    except Exception as exc:
        print("Error creating enrollment: ", exc)

#Delete an existing enrollment.
def delete_enrollment():
    id_ = input("Enter the enrollment's id: ")
    if enrollment := Enrollment.find_by_id(id_):
        enrollment.delete()
        print(f'Enrollment {id_} deleted')
    else:
        print(f'Enrollment {id_} not found')

#List all enrollments for a specific student.
def list_student_enrollments():
    try:
        student_id = int(input("Enter the student's id: "))
        enrollments = Enrollment.find_by_student_id(student_id)
        if enrollments:
            for enrollment in enrollments:
                print(enrollment)
        else:
            print("No enrollments found for the given student ID.")
    except ValueError:
        print("Invalid. Please enter a valid student ID.")

#List all enrollments for a specific course.
def list_course_enrollments():
    course_id = int(input("Enter the course's id: "))
    enrollments = Enrollment.find_by_course_id(course_id)
    for enrollment in enrollments:
        print(enrollment)