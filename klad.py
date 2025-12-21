class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f"{self.name} (ID: {self.emp_id})"
    
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    
    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"
    
    def get_info(self):
        return f"{super().get_info()}, Менеджер отдела {self.department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} выполняет обслуживание ({self.specialization})"
    
    def get_info(self):
        return f"{super().get_info()}, Техник ({self.specialization})"

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []
    
    def get_info(self):
        return f"{self.name} (ID: {self.emp_id}), Технический менеджер, Отдел: {self.department}, Специализация: {self.specialization}"
    
    def add_employee(self, employee):
        self.team.append(employee)
        return f"{employee.name} добавлен в команду"
    
    def get_team_info(self):
        if not self.team:
            return "В команде пока никого нет"
        
        result = f"Команда {self.name}:\n"
        for emp in self.team:
            result += f"- {emp.get_info()}\n"
        return result


if __name__ == "__main__":
    менеджер = Manager("Рома Синицын", "001", "IT")
    техник = Technician("Скорпион", "002", "Сети")
    техменеджер = TechManager("Кратос", "003", "Разработка", "DevOps")
    
    print("1. Информация:")
    print(менеджер.get_info())
    print(техник.get_info())
    print(техменеджер.get_info())
    
    print("\n2. Работа:")
    print(менеджер.manage_project())
    print(техник.perform_maintenance())
    print(техменеджер.manage_project())
    print(техменеджер.perform_maintenance())
    
    print("\n3. Управление командой:")
    print(техменеджер.add_employee(менеджер))
    print(техменеджер.add_employee(техник))
    print(техменеджер.get_team_info())