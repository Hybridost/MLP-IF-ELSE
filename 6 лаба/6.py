#1
# class UserAccount:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.__password = password

#     def set_password(self, new_password):
#         self.__password = new_password
#         return f"Пароль успешно изменен"

#     def check_password(self, password):
#         return password == self.__password

#     def get_account_info(self):
#         return f"Username: {self.username}, Email: {self.email} Password: {self.__password}"

# user1 = UserAccount("mail", "email", "password")
# print(user1.email)
# # print(user1.__password)
# pw = input("Введите новый пароль: ")
# print(user1.set_password(pw))

# user_input = input("Введите пароль для проверки: ")
# if user1.check_password(user_input):
#     print("Пароль верный")
#     print(user1.get_account_info())
# else:
#     print("Неверный пароль")

#2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
        def __init__(self, make, model, fuel_type):
            super().__init__(make, model)
            self.fuel_type = fuel_type

        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("Porsche 911", "911 Turbo серии 997")

car1 = Car("Toyota", "Camry", "бензин")
car2 = Car("Tesla", "Model S", "электричество")
car3 = Car("Volkswagen", "Golf", "дизель")

print("Базовый класс Vehicle:")
print(vehicle.get_info())
print(car3.get_info())