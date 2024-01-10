import json
        
def get_courses_from_file():
    with open("course_data.json", "r") as file:
        course_list = json.load(file)
    return course_list

def write_courses_to_file(course_list):
    with open("course_data.json", "w") as outfile:
        json.dump(course_list, outfile, indent=4)

def display_courses(course_list):
    print("\n")
    print("Course  Hours  Grade")
    for course in course_list:
        print(f"{course['name']:8} {course['hours']:7} {course['grade']:2}")
    
def add_course():
    course_list = []
    try:
        course_list = get_courses_from_file()
    except:
        print("No courses!")
    display_courses(course_list)
    while True:
        name = input("Enter Course Name: ")
        for course in course_list:
            if course["name"] == name:
                print("\n")
                print("Already in the database!")
                return
            
        hours = input("Credit Hours: ")
        grade = input("Grade: ")
        course = {"name": name, "hours": hours, "grade": grade}
        course_list.append(course)
        status = input("Type yes if done: ")
        if status in ['yes']:
            break
    write_courses_to_file(course_list)
    display_courses(course_list)

def calculate_gpa():
    gpa_list = [4.00, 4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.67]
    course_list = []
    try:
        course_list = get_courses_from_file()
    except:
        print("No courses!")
        return 0
    
    quality_points = 0
    gpa_hours = 0;
    for course in course_list:
        grade = course['grade']
        credit_hours = int(course['hours'])
        if grade == "A+":
            quality_points = quality_points + gpa_list[0] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "A":
            quality_points = quality_points + gpa_list[1] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "A-":
            quality_points = quality_points + gpa_list[2] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "B+":
            quality_points = quality_points + gpa_list[3] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "B":
            quality_points = quality_points + gpa_list[4] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "B-":
            quality_points = quality_points + gpa_list[5] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "C+":
            quality_points = quality_points + gpa_list[6] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "C":
            quality_points = quality_points + gpa_list[7] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "C-":
            quality_points = quality_points + gpa_list[8] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "D+":
            quality_points = quality_points + gpa_list[9] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "D":
            quality_points = quality_points + gpa_list[10] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "D-":
            quality_points = quality_points + gpa_list[11] * credit_hours
            gpa_hours = gpa_hours + credit_hours
        elif grade == "F":
            quality_points = quality_points + gpa_list[12] * credit_hours
            gpa_hours = gpa_hours + credit_hours
    gpa = quality_points / gpa_hours
    print("\n")
    print("GPA:")
    print(gpa)
