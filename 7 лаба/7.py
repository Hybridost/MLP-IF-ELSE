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
        self.team = []
    
    def manage_project(self):
        return f"{self.name} управляет проектами в отделе {self.department}"
    
    def add_employee(self, employee):
        self.team.append(employee)
    
    def get_team_info(self):
        return [emp.get_info() for emp in self.team]


class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        self.department = department
        self.specialization = specialization
        self.team = []


# Демонстрация работы
emp1 = Employee("Иван Гамаз", 100)
manager = Manager("Тайдхантер", 101, "IT")
tech = Technician("Петр 1", 102, "Сети")
tech_manager = TechManager("Сергэй", 103, "Разработка", "DevOps")

print(emp1.get_info())
print(manager.manage_project())
print(tech.perform_maintenance())

tech_manager.add_employee(emp1)
tech_manager.add_employee(tech)
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print(f"Команда {tech_manager.name}: {tech_manager.get_team_info()}")