# TODO
# 1. Download Git
# 2. Install Git extension on VSCode
# 3. If you are using Windows, activate WSL on your machine.
# 4. Start WSL and practire some of the command lines on the terminal
# dir
# ls 
# mkdir
# touch
# cd 
# cd ..

# if you are using MAC, you should be able to open MAC terminal
# by typing CMD + <space>


# Question (Time complexities)
# For each method for Employee and Company classes, figure out the best and worst case time complexities

class Employee:

    def __init__(self, name: str, empID: int, salary=100.0):
        # Best Case: 1 — assigning values
        # Worst Case: 1 — assigning values
        self.name = name
        self.empID = empID
        self.salary = salary
        self.skillset = set()

    def add_skill(self, skill: str) -> None:
        # Best Case: 1 — adding to a set
        # Worst Case: 1 — adding to a set
        self.skillset.add(skill)

    def remove_skill(self, skill):
        # Best Case: 1 — skill not in set
        # Worst Case: 1 — skill is found and removed
        if skill in self.skillset:
            self.skillset.remove(skill)

    def increase_salary(self, increase_amount=10):
        # Best Case: 1 — updating a number
        # Worst Case: 1 — updating a number
        self.salary += increase_amount

    def __lt__(self, other):
        # Best Case: 1 — comparing two numbers
        # Worst Case: 1 — comparing two numbers
        return self.salary < other.salary

    def __str__(self):
        # Best Case: 1 — empty skillset
        # Worst Case: n — converting n skills to string
        return f"Employee Information\n" f"Name: {self.name}\n" f"Employee ID: {self.empID}\n" f"Salary: ${self.salary}\n" f"Skills: {self.skillset}\n"


class Company:

    ID_COUNTER = 1000

    def __init__(self, company_name):
        # Best Case: 1 — assigning values
        # Worst Case: 1 — assigning values
        self.company_name = company_name
        self.employee_list = []
        self.id_counter = 1000

    def hire(self, person_name: str, salary: float):
        # Best Case: 1 — creating and adding new employee
        # Worst Case: 1 — creating and adding new employee
        e = Employee(person_name, Company.ID_COUNTER, salary)
        Company.ID_COUNTER += 1
        self.employee_list.append(e)

    def get_employee_count(self) -> int:
        # Best Case: 1 — getting length of a list
        # Worst Case: 1 — getting length of a list
        return len(self.employee_list)

    def total_compansation(self) -> float:
        # Best Case: n — sum all salaries once
        # Worst Case: n — sum all salaries once
        total = 0
        for e in self.employee_list:
            total += e.salary
        return total

    def max_salaried_employee(self) -> "Employee":
        # Best Case: n — check all salaries once
        # Worst Case: n — check all salaries once
        if len(self.employee_list) == 0:
            return None

        current_max = 0
        current_employee = None

        for e in self.employee_list:
            if e.salary > current_max:
                current_max = e.salary
                current_employee = e

        return current_employee

    def __str__(self):
        # Best Case: 1 — empty employee list
        # Worst Case: n — build string from list of n employees
        summary = f"Company: {self.company_name}; Employee count: {self.employee_list}"
        return summary