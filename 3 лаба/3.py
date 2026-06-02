# 1 ЗАДАНИЕ
# Чтение всего файла

# with open('C:/Users/Amor/Desktop/example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# # Чтение строк
# with open('C:/Users/Amor/Desktop/example.txt', 'r') as file:
#     for line in file:
#         print(f"Строка: {line.rstrip()}")

# # Чтение по выбору
# def read_file(filename, method='all'):
#     with open(filename, 'r') as file:
#         if method == 'all':
#             return file.read()
#         elif method == 'line':
#             return [line.strip() for line in file]

# print(read_file('C:/Users/Amor/Desktop/example.txt', 'all')) 
# print(read_file('C:/Users/Amor/Desktop/example.txt', 'line')) 

# 2 ЗАДАНИЕ
# Запись нового файла

# text = input("Введите текст: ")
# with open('sema.txt', 'w') as f:
#     f.write(text)

# Запись в уже существующий файл

# new_text = input("Введите текст для добавления: ")
# with open('sema.txt', 'a') as f:
#     f.write("\n" + new_text)

# 3 ЗАДАНИЕ

def read_file_safe(filename, method='all'):
    try:
        if method == 'all':
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        elif method == 'line':
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")

read_file_safe('C:/Users/Amor/Desktop/examplde.txt','line')


# 2

# def write_to_file(filename, content, mod):
#     if mod == '1':
#         with open(filename, 'w') as f:
#             f.write(content)
#     elif mod == '2':
#         with open(filename, 'a') as f:
#             f.write("\n" + content)

# method = input("Выберите метод (1 - запись нового файла, 2 - добавление текста): ")
# text = input("Введите текст: ")
# write_to_file('sema.txt', text, method)
