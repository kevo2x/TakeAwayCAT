class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department is: {total}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()

# Interactive system to manage employees and departments
def main():
    # Sample department
    department = Department(input("Enter department name: "))

    while True:
        print("\nEmployee Management System")
        print("1. Add an employee")
        print("2. Update employee salary")
        print("3. Display total salary expenditure")
        print("4. Display all employees")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            employee_id = input("Enter employee ID to update salary: ")
            new_salary = float(input("Enter new salary: "))
            employee = next((e for e in department.employees if e.employee_id == employee_id), None)
            if employee:
                employee.update_salary(new_salary)
            else:
                print("Employee not found.")

        elif choice == "3":
            department.calculate_total_salary_expenditure()

        elif choice == "4":
            department.display_all_employees()

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()