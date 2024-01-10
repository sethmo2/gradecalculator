import json
        
def get_courses_from_file(course_list):
    with open("course_data.json", "r") as file:
        course_list = json.load(file)
    return course_list

def write_courses_to_file(course_list):
    with open("course_data.json", "w") as outfile:
        json.dump(course_list, outfile, indent=4)

def display_courses(course_list):
    for course in course_list:
        print(f"{course['name']:8} {course['hours']:1} {course['grade']:2}")

def add_course():
    course_list = []
    try:
        course_list = get_courses_from_file(course_list)
    except:
        print("No courses!")
    display_courses(course_list)
    while True:
        name = input("Enter Course Name: ")
        hours = input("Credit Hours: ")
        grade = input("Grade: ")
        course = {"name": name, "hours": hours, "grade": grade}
        course_list.append(course)
        status = input("Type yes if done: ")
        if status in ['yes']:
            break
    write_courses_to_file(course_list)
    display_courses(course_list)
