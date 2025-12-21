
def greet(name):
    return f"Привет, {name}!"

def square(number):
    return number ** 2

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y


def describe_person(name, age=30):
    print(name + " - " + str(age) + " лет")


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

name = input()
age = input()
if age: print(describe_person(name, age))
else:print(describe_person(name))
# print(greet("Ромчик"))

# print(square(6.9))

# print(max_of_two(22, 8))


# describe_person("Уйзунбек", 25)
# describe_person("Саб-зиро")  

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(13))