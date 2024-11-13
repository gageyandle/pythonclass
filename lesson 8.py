import csv

# shows the startup statement, 1-5 options text, and prompts for user input, then on input performs the choice, breaking on selction of number 5 and printing the completed by message.
def main(): 
    print("Welcome to the Contact Manager!")
    while True: 
        print("1 - Create a new contact")
        print("2 - Add a new contact")
        print("3 - Read all the contacts")
        print("4 - Modify an existing contact")
        print("5 - Exit")
        choice = input("Select an option:  ")
        if choice == "1": 
            create_csv_file()
        elif choice == "2": 
            add_contact()
        elif choice == "3": 
            view_contacts()
        elif choice == "4": 
            edit_contact()
        elif choice == "5": 
            break
        else: 
            print("Invalid option, try again.")
    print("Completed by,  Gage Yandle")

# below creates the csv file, prints success.
def create_csv_file(): 
    with open('contacts.csv',  'w',  newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(['Name',  'Phone',  'Email'])
    print("File created successfully.")

# below collects input from user on name, phone number, and email, prints success.
def add_contact(): 
    name = input("Enter name:  ")
    phone = input("Enter phone:  ")
    email = input("Enter email:  ")
    with open('contacts.csv',  'a',  newline='') as file: 
        writer = csv.writer(file)
        writer.writerow([name,  phone,  email])
    print("Contact added successfully.")

# below views the contents of the 
def view_contacts(): 
    with open('contacts.csv',  'r') as file: 
        reader = csv.reader(file)
        for row in reader: 
            print(row)

# below allows you to edit the contact you have already entered into the file
def edit_contact(): 
    view_contacts()
    contact_to_edit = input("Enter the name of the contact you want to edit:  ")
    with open('contacts.csv',  'r') as file: 
        reader = csv.reader(file)
        contacts = list(reader)
    contact_found = False
    for i,  contact in enumerate(contacts): 
        if contact[0] == contact_to_edit: 
            contact_found = True
            new_email = input("Enter new email:  ")
            new_phone = input("Enter new phone:  ")
            contacts[i] = [contact[0],  new_phone,  new_email]
            break
    if contact_found: 
        with open('contacts.csv',  'w',  newline='') as file: 
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact edited successfully.")
    else: 
        print("Contact not found.")

if __name__ == "__main__": 
    main()
