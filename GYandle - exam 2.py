def main():   
    import random
    employees = []
    existing_employee_ids = []
    existing_employee_names = []
    num_employees = int(input("Enter the number of new employees being added to the company: "))
        #Prints the start of the program as well as collecting the input.
    
    
    def create_employee(employees, existing_employee_ids, existing_employee_names):   
        while True:   
            name = input("Enter the employee's name: ")
            if name.lower() in [employee['name'].lower() for employee in employees]:   
                print("Employee already exists. Please enter a different name.")
                #Checks if the name entered has been entered before, and also takes in to count capital letters.
            else:   
                existing_employee_names.append(name)
                break
                
        while True:   
            id_num = random.randint(1,500)
            if id_num not in existing_employee_ids:   
                existing_employee_ids.append(id_num)
                break
                #Assigns random ID and removes an ID if it has been generated before.
        employee = {'name': name, 'id': id_num}
        employees.append(employee)
    
    def employee_output(employee): 
        return f"Employee {employee['name']} has been created with ID {employee['id']}"
    
    for _ in range(num_employees):   
        create_employee(employees, existing_employee_ids, existing_employee_names)
         #Loop
    print("Employee list: ")
    for employee in employees:   
        print(employee_output(employee))
    
    print("Completed by Gage Yandle")

if __name__ == "__main__":   
    main()
