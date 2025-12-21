# 1

def greet(name):
    print("Привет, " + name + "!")

def square(number):
    return number * number

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y


# 2

def describe_person(name, age=30):
    return ("Имя: " + name + ", Возраст: " + str(age))
name = input()
age = input()
if age : 
    print(describe_person(name, age))
else:
    print(describe_person(name))



# 3

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True


# Примеры 
# greet("Ярослав")
# print(square(5))
# print(max_of_two(3, 7))

# describe_person("Вика", 25)
# describe_person("Рома")

# print(is_prime(17))  
# print(is_prime(15))  
