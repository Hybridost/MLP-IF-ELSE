def greet(name):
    return f"Привет, {name}!"
print(greet("Скорпион"))


def square():
    a = int(input("Введите число: "))
    return a*a

number = square()
print("Квадрат числа:", number)


def max_of_two():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    return max(a,b)

max_number = max_of_two()
print("Большее число:", max_number)


def describe_person(name, age=30):
    print(name + " - " + str(age) + " лет")
name = input()
age = input()
if age: print(describe_person(name, age))
else:print(describe_person(name))


def is_prime(number):
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for k in range(3, int(number**0.5) + 1, 2):
        if number % k == 0:
            return False
    
    return True

print(is_prime(4))    
print(is_prime(9))    
print(is_prime(20))   
print(is_prime(15))   
print(is_prime(35))   
print(is_prime(3))    
print(is_prime(0)) 
print(is_prime(7))