import random

def main(): 
    grades = []

    while True: 
        grade = input("Enter a grade (or -1 to stop):  ")
        if grade == "-1": 
            break
        else: 
            grades.append(float(grade))

    print("Original grades: ",  grades)

    print("\nRemoving the lowest grade: ")
    lowest_grade = min(grades)
    grades.remove(lowest_grade)
    print("Grades after removing the lowest: ",  grades)

    print("\nRemoving a random grade: ")
    random.shuffle(grades)
    grades.pop()
    print("Grades after removing a random grade: ",  grades)

    print("\nEditing a grade: ")
    for i,  grade in enumerate(grades): 
        print(f"{i+1}. {grade}")

    while True: 
        try: 
            edit_index = int(input("Enter the number of the grade you would like to edit:  ")) - 1
            if 0 <= edit_index < len(grades): 
                break
            else: 
                print("PLease enter a valid grade number,  try again.")
        except ValueError: 
            print("Invalid input. Please enter a number.")

    new_grade = float(input("Enter the new grade:  "))
    grades[edit_index] = new_grade
    print("Grades after editing: ",  grades)

    print("\nSorting and reversing the list: ")
