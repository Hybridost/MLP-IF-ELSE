# #ЗАДАНИЕ 1

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
    
book1 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book2 = Book("1984", "Джордж Оруэлл", 1949)
book3 = Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943)
    
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


#ЗАДАНИЕ 2

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_radius(self):
#         return self.radius
    
#     def set_radius(self, new_radius):
#         self.radius = new_radius

# if __name__ == "__main__":
    
#     circle1 = Circle(5.0)
#     print(f"Начальный радиус: {circle1.get_radius()}")

#     circle1.set_radius(7.5)
#     print(f"Новый радиус: {circle1.get_radius()}")