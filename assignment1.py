# STEP 1: Initialize Data Storage 
# We use a dictionary where the 'Key' is the ID and the 'Value' is another dictionary.
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

# STEP 2: The Main Program Loop
# This loop keeps the program running until the user chooses to exit.
while True:
    print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
    print("1. Add a New Employee")
    print("2. View All Employees")
    print("3. Search for an Employee")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
 
    # STEP 3: Add Employee Logic
    if choice == '1':
        # Get ID and check if it already exists
        emp_id = int(input("Enter Employee ID: "))
        
        if emp_id in employees:
            print("Error: This ID already exists. Please use a unique ID.")
        else:
            # Get other details
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            
            # Store the data inside the dictionary
            employees[emp_id] = {
                'name': name, 
                'age': age, 
                'department': dept, 
                'salary': salary
            }
            print("Employee added successfully!")

    # STEP 4: View All Employees Logic
    elif choice == '2':
        print("\n--- All Employee Records ---")
        if not employees:
            print("No employees found in the system.")
        else:
            # Loop through the dictionary to print each employee
            for eid, info in employees.items():
                print(f"ID: {eid} | Name: {info['name']} | Dept: {info['department']} | Salary: {info['salary']}")

    # STEP 5: Search Logic
    elif choice == '3':
        search_id = int(input("Enter the Employee ID to search: "))
        
        if search_id in employees:
            # Fetch the data using the ID (Key)
            emp = employees[search_id]
            print(f"Details found - Name: {emp['name']}, Dept: {emp['department']}, Age: {emp['age']}")
        else:
            print("Employee not found.")

    # STEP 6: Exit Logic
    elif choice == '4':
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

print("program end here ! thank you .")        



