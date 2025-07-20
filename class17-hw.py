# Question
# Given all the below information create one or more classes to model the real life problem. 

# Narration
# Your company has grown significantly, and you need to streamline workforce tracking and management. 
# You have been tasked to build and use a programmatic model of the company's employees, their roles, 
# and their working relationships. Your objective is to manage different types of employees, track 
# their attributes, and perform actions such as promotions, skill tracking, and personnel 
# management effectively. Additionally, your model should allow creating employees from 
# external data sources (e.g., files), and support hierarchical relationships within the workforce.


# Requirements:
# Employees and Their Attributes:

#   - Each employee is an individual with a name, age, and salary.
#   - Some employees have specialized roles, such as Engineers, Managers, etc.
#   - Make sure to account for any specific behaviors unique to these specialized roles (e.g., Engineers have skills).


# Tracking Population:
#   - Track the overall population of individuals in your system globally, regardless of their positions within the company.

# Managerial Hierarchies:
#   - Managers oversee teams, which consist of other employees.
#   - Managers should be able to add team members and count the number of employees they manage.

# Engineers and Skills:
#   - Engineers bring specialized skills to the team (e.g., programming languages, technologies). Skills should be properly tracked and expandable over time.

# Company Entity:
#   - Employees collectively form a company. The company should have the ability to:
#   - Add and remove employees.
#   - Promote all employees simultaneously to boost morale and performance (e.g., increase salaries).

# Actions and Behaviors:
#   - Employees should be able to take specific actions (e.g., increase their age or salary).
#   - Managers should extend their teams dynamically via a structured system.
#   - Engineers should update their skill sets over time.

# Data Input:
#   - Use external data sources (string or file-based data) to initialize entities in your system, such as creating employees with their basic attributes.

class Employee:
    population = []

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.population.append(self)

    def increase_salary(self, amount):
        if 0 < amount < 10000:
            self.salary += amount

    def increase_age(self, years):
        if 0 < years < 5:
            self.age += years

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Salary: {self.salary}"

    @classmethod
    def get_population(cls):
        return len(cls.population)


class Engineer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.skills = []

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)


class Manager(Employee):
    team = []

    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        

    def add_team_member(self, employee):
        if employee not in Manager.team:
            Manager.team.append(employee)

    def team_size(self):
        return len(self.team)



class Company(Employee):
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def add_employee(cls, employee):
        if isinstance(employee, Employee):
            Employee.population.append(employee)

    @classmethod
    def remove_employee(cls, employee):
        if employee in Employee.population:
            Employee.population.remove(employee)
            if employee in Manager.team:
                Manager.team.remove(employee)


    @classmethod
    def promote_all(cls, amount):
        for employee in Employee.population:
            Employee.increase_salary(employee, amount)

    def __str__(self):
        summary = f"Company: {self.name}\n"
        return summary


# Function to create employees from a data string or file line
def create_employee_from_data(line):
    # Format: role,name,age,salary,skill1,skill2
    parts = line.strip().split(",")
    role = parts[0].lower()
    name = parts[1]
    age = int(parts[2])
    salary = int(parts[3])
    if role == "engineer":
        engineer = Engineer(name, age, salary)
        if len(parts) > 4:
            for skill in parts[4].split(","):
                engineer.add_skill(skill)
        return engineer
    elif role == "manager":
        return Manager(name, age, salary)
    else:
        return Employee(name, age, salary)
    

first_employee = Employee('John Macdonald', 87, 56000)
print(Employee.get_population())  # 1
first_employee.increase_salary(2000)
first_employee.increase_age(5)
print(first_employee)  # John Macdonald, Age: 87, Salary: 58000

second_employee = Engineer('Hoover', 19, 33000)
print(Employee.population)  # [<__main__.Employee object at 0x100a41d00>, <__main__.Engineer object at 0x100a41d60>]
print(Employee.get_population())  # 2
second_employee.add_skill('welding')
print(second_employee.skills)  # ['welding']

third_employee = Manager('Brenda', 56, 98000)
print(Employee.get_population())  # 3
third_employee.add_team_member(second_employee)
print(third_employee.team)  # [<__main__.Engineer object at 0x100a41d60>]
print(third_employee.team_size())  # 1

first_company = Company('Dunder Mifflin')
print(Employee.get_population())  # 4
first_company.remove_employee(second_employee)
print(Employee.get_population())  # 3
print(len(Manager.team))  # 0
