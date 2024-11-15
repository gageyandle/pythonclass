def main():

    student_info = {}

    # student information to the dictionary
    student_info["Paul"] = {"ID": 1, "GPA": 3.8, "Credits": 60, "Grades": ["80", "85", "90", "75"]}
    student_info["Bill"] = {"ID": 6, "GPA": 3.2, "Credits": 45, "Grades": ["80", "75", "90", "80"]}
    student_info["Harry"] = {"ID": 5, "GPA": 3.5, "Credits": 55, "Grades": ["95", "90", "85", "75"]}

    # dictionary containing all student information
    print("Student Information Dictionary:")
    print(student_info)

    print("\nStudent Names:")
    for name in student_info:
        print(name)

    # print a heading for accessing student information
    #  \t is an escape sequence that represents a horizontal tab character
    print("\nStudent Information:")
    print("Name\tID\tGPA\tCredits\tGrades")
    for name, info in student_info.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits']}\t{info['Grades']}")

    print("\nRemoving Student:")
    student_info.pop("Paul")
    print("Updated Student Information Dictionary:")
    print(student_info)

    print("\nAccessing GPA Information:")
    for name, info in student_info.items():
        print(f"{name}'s GPA: {info.get('GPA')}")

    # clearing the student registry
    print("\nClearing Student Registry")
    student_info.clear()
    print("Student Information Dictionary:")
    print(student_info)

    print("\nCompleted by, Gage Yandle")
if __name__ == "__main__":
    main()



