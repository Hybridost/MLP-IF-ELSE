# Способ 1: Импорт модулей
print("1. Импорт модулей:")
from my_package import numbers
from my_package import strings

result1 = numbers.add(10, 5)
print(f"   numbers.add(10, 5) = {result1}")

result2 = numbers.multiply(4, 3)
print(f"   numbers.multiply(4, 3) = {result2}")

result3 = strings.concatenate("Hello", "World")
print(f"   strings.concatenate('Hello', 'World') = '{result3}'")

result4 = strings.uppercase("alo")
print(f"   strings.uppercase('alo') = '{result4}'")


# Способ 2: Импорт функций
print("2. Импорт функций:")
from my_package.numbers import power
from my_package.strings import reverse_string

result5 = power(2, 3)
print(f"   power(2, 3) = {result5}")

result6 = reverse_string("Yarik")
print(f"   reverse_string('Yarik') = '{result6}'")


# Способ 3: Импорт с псевдонимом
print("3. Импорт с псевдонимами:")
import my_package.numbers as num
import my_package.strings as str_ops

result7 = num.add(15, 25)
print(f"   num.add(15, 25) = {result7}")

result8 = str_ops.reverse_string("Apple")
print(f"   str_ops.reverse_string('Apple') = '{result8}'")