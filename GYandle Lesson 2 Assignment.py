import os

first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")
current_year = int(input ("Enter the current year: "))
birth_year = int(input ("Enter your birth year: "))
age = current_year - birth_year 
age_string = str(age)
print ("Completed by " + first_name + " " + last_name + " they are " + age_string + " years old.")

os.system("pause")
