class Employee:

    def __init__(self, name: str, salary: int | float):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee name: {self.name}, employee salary: {self.salary}"


class Manager(Employee):

    def __init__(self, name: str, salary: int | float, department: str):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, employee department: {self.department}"


class Developer(Employee):

    def __init__(self, name: str, salary: int | float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"{super().__str__()}, employee programming language: {self.programming_language}"


class TeamLead(Manager, Developer):

    def __init__(self, name: str, salary: int | float, department: str, programming_language: str, team_size: int):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return f"{Employee.__str__(self)}, employee department: {self.department}, employee programming language: {self.programming_language}, employee team size: {self.team_size}"



employee = Employee(name="Vlad", salary=1000)
print(employee)

manager = Manager(name="Serhii", salary=2000, department="IT")
print(manager)

developer = Developer(name="Andrii", salary=3000, programming_language="Python")
print(developer)

team_lead = TeamLead(name="Vasyl",salary=5000, department="IT", programming_language="Python", team_size=4)
print(team_lead)