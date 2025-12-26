class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f"{self.department}"

    def manage_project(self):
        return f"{self.name} управляет проектами в отделе {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет тех. обслуживание по специализации: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        info = "Информация о команде:\n"
        for emp in self.subordinates:
            info += emp.get_info() + "\n"
        return info

emp1 = Employee("Анна", 101)
emp2 = Employee("Антон", 102)
mgr = Manager("Виктор", 201, "Продажи")
tech = Technician("Владимир", 301, "Сети")
tm = TechManager("Дмитрий", 401, "ИТ", "Серверы")

tm.add_employee(emp1)
tm.add_employee(emp2)
tm.add_employee(mgr)
tm.add_employee(tech)

print(tm.get_info())
print(tm.manage_project())
print(tm.perform_maintenance())
print(tm.get_team_info())

print(emp1.get_info())
print(mgr.get_info())