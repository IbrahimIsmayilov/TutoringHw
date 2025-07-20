# s = set()
# s.

class Employee:
    
    def __init__(self, name: str, empID: int, salary=100.0):
        self.name = name
        self.empID = empID
        self.salary = salary
        self.skillset = set()

    def add_skill(self, skill: str) -> None:
        self.skillset.add(skill)

    def remove_skill(self, skill):
        if skill in self.skillset:
            self.skillset.remove(skill)

    def increase_salary(self, increase_amount=10):
        self.salary += increase_amount

    def __lt__(self, other):
        return self.salary < other.salary
    
    def __str__(self):
        return f"Employee Information\n" f"Name: {self.name}\n" f"Employee ID: {self.empID}\n" f"Salary: ${self.salary}\n" f"Skills: {self.skillset}\n"

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


# Every employee in the company must have a unique ID!

# All the employees accross all the companies MUST have unique ID!

class Company:
    
    ID_COUNTER = 1000
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_list = []
        # self.id_counter = 1000

    def hire(self, person_name: str, salary: float):
        # 1. Create an employee
        e = Employee(person_name, Company.ID_COUNTER, salary)
        Company.ID_COUNTER += 1
        # 2. Add the employee to the employee_list
        self.employee_list.append(e)

    def get_employee_count(self) -> int:
        return len(self.employee_list)
    
    def total_compansation(self) -> float:
        total = 0
        for e in self.employee_list:
            total += e.salary
        return total
    
    def max_salaried_employee(self) -> "Employee":
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
        summary = f"Company: {self.company_name}; Employee count: {self.employee_list}"
        return summary

    # @classmethod
    # def tell_population(cls):
    #     return f"Company has {cls.population} employees"
    
    # def hire_employee(self):
    #     pass
    
c = Company("Google")
c.hire("Osman", 150)
c.hire("Leyla", 150)
print(c.total_compansation())

e = c.max_salaried_employee()
e.increase_salary(200)

print(c.total_compansation())

# Worst case: len(lst)
# Best case: 1
def foo(lst: list, n: int) -> bool:
    return n in lst

# Wrost case: len(lst) * len(lst) = len(lst) ** 2
# Best case: len(lst) * 1 = len(lst)
def qoo(lst):
    for elem in lst: # len(lst), len(lst)
        if "a" in lst: # len(lst),  1
            print("a is in the list")
            
def dummy(lst):
    for n in lst:
        pass

def qoo(lst):
    for elem in lst: # len(lst), len(lst)
        if dummy(lst): # len(lst),  len(lst)
            print("a is in the list")
            

# Git: version control


# bash commands:
# dir
# ls 
# mkdir
# touch
# cd 
# cd ..


#  Untracked changes  (by git add)->   Git staging area  (git commit) ->