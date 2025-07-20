# Question (Employee class)
# Design an "Employee" class. 
# - Each employee have their name, salary and employee ID.
# - Each employee should also have skillset. Example skillset for an employee would be: Word, Python, English and etc.
# - Note that there might be more than one skill that an employee posesses.
# - You should be able to add and remove a skillset for an employee.
# - You should also be able to increase an employee salary.
# - Must have nice printing
# - You should be able to compare the Employees to each other by salary.
# Employee class
class Employee:
    _id_counter = 1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_id = Employee._id_counter
        Employee._id_counter = Employee._id_counter + 1
        self.skillset = set()

    def add_skill(self, skill):
        self.skillset.add(skill)

    def remove_skill(self, skill):
        if skill in self.skillset:
            self.skillset.remove(skill)

    def increase_salary(self, amount):
        if amount > 0:
            self.salary = self.salary + amount

    def __str__(self):
        skills = ""
        if len(self.skillset) == 0:
            skills = "No skills"
        else:
            sorted_skills = sorted(self.skillset)
            index = 0
            for skill in sorted_skills:
                skills = skills + skill
                index = index + 1
                if index < len(sorted_skills):
                    skills = skills + ", "
        return "Employee ID: " + str(self.employee_id) + ", Name: " + self.name + ", Salary: $" + str(self.salary) + ", Skills: " + skills

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary


# Question (Company class)
# Design a "Company" class.
# - Each company should have a name and list of employees.
# - Each company should be able to hire and fire an employee.
    # - Implement this as a method where we get a string name and salary as method parameters: def hire(self, person_name: str, salary: int)
    # - Firing should be happening based on an employee ID
# - Should be able to tell how many people are working for the company
# - Should be able to tell how much is the total compensation of its employees.
# - Should be able to tell who is the highest salaried employee.
# - Must have nice printing
# Company class
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, person_name, salary):
        new_emp = Employee(person_name, salary)
        self.employees.append(new_emp)
        return new_emp

    def fire(self, emp_id):
        new_list = []
        for emp in self.employees:
            if emp.employee_id != emp_id:
                new_list.append(emp)
        self.employees = new_list

    def employee_count(self):
        count = 0
        for emp in self.employees:
            count = count + 1
        return count

    def total_compensation(self):
        total = 0
        for emp in self.employees:
            total = total + emp.salary
        return total

    def highest_paid_employee(self):
        if len(self.employees) == 0:
            return None
        highest = self.employees[0]
        for emp in self.employees:
            if emp.salary > highest.salary:
                highest = emp
        return highest

    def __str__(self):
        result = "Company: " + self.name + "\n"
        result = result + "Total Employees: " + str(self.employee_count()) + "\n"
        result = result + "Employees:\n"
        for emp in self.employees:
            result = result + str(emp) + "\n"
        return result


# Question (Time complexities)
# For each function below:
# - Describe when the function reaches its best case time complexity and worst case time complexity
# - What are the best and worst case time complexities? 
# Best Case: 1 — if n is the first element in the list
# Worst Case: n — if n is not in the list or is the last element
def foo(lst: list, n: int) -> bool:
    return n in lst

# Best Case: n — even if "a" is found early, the check runs every iteration
# Worst Case: n^ 2— "a" in lst of n size is checked in every iteration n times
def qoo(lst):
    for elem in lst:
        if "a" in lst:
            print("a is in the list")