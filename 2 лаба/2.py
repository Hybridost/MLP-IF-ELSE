def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(x, y):
    return max(x, y)

def describe_person(name, age=30):
    print(f"{name}, {age} лет")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Тест greet
greet("Артас")

# Тест square
print(f"Квадрат числа 4: {square(4)}")
print(f"Квадрат числа 9: {square(9)}")

# Тест max_of_two
print(f"Большее из 3 и 7: {max_of_two(3, 7)}")
print(f"Большее из -5 и 2: {max_of_two(-5, 2)}")

# Тест describe_person
describe_person("Колян", 35)
describe_person("Мотя")

# Тест is_prime
numbers = [2, 3, 4, 5, 17, 20, 29]
for num in numbers:
    print(f"Число {num}: {'простое' if is_prime(num) else 'не простое'}")