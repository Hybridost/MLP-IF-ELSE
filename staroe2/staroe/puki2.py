class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f"{self.name} (ID: {self.id})"


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
    
    def manage_project(self, project_name):
        return f"{self.name} управляет проектом {project_name}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} делает техобслуживание"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        self.specialization = specialization
        self.team = []  
    
    def add_employee(self, employee):
        self.team.append(employee)
        print(f"Добавил {employee.name} в команду")
    
    def get_team_info(self):
        print(f"Команда {self.name}:")
        for emp in self.team:
            print(f"  - {emp.get_info()}")

worker = Employee("Иван", 1)
boss = Manager("Анна", 2, "IT")
tech = Technician("Петр", 3, "сети")
tech_boss = TechManager("Сергей", 4, "IT", "базы данных")

print(worker.get_info())
print(boss.get_info())
print(tech.get_info())
print(tech_boss.get_info())

print(boss.manage_project("Сайт компании"))
print(tech.perform_maintenance())
print(tech_boss.manage_project("Обновление БД"))
print(tech_boss.perform_maintenance())


tech_boss.add_employee(worker)
tech_boss.add_employee(tech)
tech_boss.get_team_info()