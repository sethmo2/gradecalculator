import json
from actions import *

while True:
    print("Options:")
    print("0: Exit")
    print("1: View Courses")
    print("2: Add a Course")
    print("3: Calculate GPA")
    user_choice = input("What would you like to do?: ")
    if user_choice == "0":
        break
    if user_choice == "1":
        course_list = []
        course_list = get_courses_from_file()
        display_courses(course_list)
    if user_choice == "2":
        add_course()
    if user_choice == "3":
        calculate_gpa()