
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

class Company:
    
    ID_COUNTER = 1000
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_list = []
        self.id_counter = 1000

    def hire(self, person_name: str, salary: float):
        e = Employee(person_name, Company.ID_COUNTER, salary)
        Company.ID_COUNTER += 1
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
    

# What is time complexity of removing and adding an element to the end of the list?
# Constant: 1 time complexity
lst = []



[10, 20, 30].remove(30)

[10, 20, 30].remove(10)

# Removal when we know the index of the element that we are trying to remove
# 2 types of removals from the list
# 1. Preserves the order

[5, 10, 20, 30]
[20, 30, 30]
[20, 30]

[5, 10, 20, 30]
[5, 20, 30, 30]

[5, 30, 20, 10]
[5, 30, 20]

# 1. Find the element
# 2. Remove the element at that index, preserving the oder

lst = [5, 30, 20]
lst = [20, 30, 5]
# i iterations to find the element. It will also take len(lst) - i iterations to remove it
# i + len(lst) - i = len(lst)
lst = [20, 5, 30]
lst.remove(5)
print(lst)



# When we are talking about time complexity we are interested in the largest contributor to the time complexity
# 1 + 5 = 6 => treat this as constant. Just call it 1.


# len(lst) * len(lst) + 1: 

# len(lst) * len(lst) + len(lst): n ** 2 + n: n ** 2


# n**3 + n**2 + n + 1 =>  n**3

# n + 1 => n 
# n => n

def foo(lst):
    a = 5

def foo(lst):
    a = 5
    b = 7
    
# It takes a constant time to remove from set.


my_dictionary = {"a": 5, "b": 5, "c": 7}
del my_dictionary["c"] # Constant time
# command line arguments

# Git commands
# git status
# git commit -m "<commit message>"
# git add
# git log
# git checkout <commit id>