import json
from actions import *

while True:
    print("Options:")
    print("0: Exit")
    print("1: View Courses")
    print("2: Add a Course")
    print("3: Remove a Course")
    print("4: Calculate GPA")
    user_choice = input("What would you like to do?: ")
    if user_choice == "0":
        break
    elif user_choice == "1":
        course_list = []
        course_list = get_courses_from_file()
        display_courses(course_list)
    elif user_choice == "2":
        add_course()
        print("\n")
    elif user_choice == "3":
        remove_course()
        print("\n")
    elif user_choice == "4":
        calculate_gpa()
        print("\n")
    else:
        print("\n")
        print("Enter a valid option")
        print("\n")