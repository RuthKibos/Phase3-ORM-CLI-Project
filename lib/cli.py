from helpers import (
    exit_program,
    list_students,
    find_student_by_name,
    find_student_by_id,
    create_student,
    update_student,
    delete_student,
    list_courses,
    find_course_by_name,
    find_course_by_id,
    create_course,
    update_course,
    delete_course,
    list_enrollments,
    find_enrollment_by_id,
    create_enrollment,
    delete_enrollment,
    list_student_enrollments,
    list_course_enrollments
)

#Main function to handle the user input and call the appropriate helper functions.
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            list_courses()
        elif choice == "8":
            find_course_by_name()
        elif choice == "9":
            find_course_by_id()
        elif choice == "10":
            create_course()
        elif choice == "11":
            update_course()
        elif choice == "12":
            delete_course()
        elif choice == "13":
            list_enrollments()
        elif choice == "14":
            find_enrollment_by_id()
        elif choice == "15":
            create_enrollment()
        elif choice == "16":
            delete_enrollment()
        elif choice == "17":
            list_student_enrollments()
        elif choice == "18":
            list_course_enrollments()
        else:
            print("Invalid choice")

 #Display the menu options to the user
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all students")
    print("2. Find student by name")
    print("3. Find student by id")
    print("4. Create student")
    print("5. Update student")
    print("6. Delete student")
    print("7. List all courses")
    print("8. Find course by name")
    print("9. Find course by id")
    print("10. Create course")
    print("11. Update course")
    print("12. Delete course")
    print("13. List all enrollments")
    print("14. Find enrollment by id")
    print("15. Create enrollment")
    print("16. Delete enrollment")
    print("17. List all enrollments for a student")
    print("18. List all enrollments for a course")

if __name__ == "__main__":
    main()