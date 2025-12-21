def greet():
    a = input("Как вас зовут? ")
    return a

name = greet()
print("Привет,", name)


def square():
    a = int(input("Введите число: "))
    return a**2

number = square()
print("Квадрат этого числа:", number)


def max_of_two():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return max(a,b)

max_number = max_of_two()
print("Большее число:", max_number)


def describe_person(name, age=30):
    print(f'Имя: {name}, Возраст: {age}')



def is_prime(number):
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True

print(is_prime(2))    
print(is_prime(7))    
print(is_prime(10))   
print(is_prime(17))   
print(is_prime(25))   
print(is_prime(1))    
print(is_prime(0)) 