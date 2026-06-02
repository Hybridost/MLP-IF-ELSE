import numpy as np
import time

print("Задание 1")
a = np.array([10, 20, 30, 40, 50, 60])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(f"Массив a: ndim={a.ndim}, shape={a.shape}, dtype={a.dtype}, size={a.size}")
print(f"Массив b: ndim={b.ndim}, shape={b.shape}, dtype={b.dtype}, size={b.size}")
print("Срез b (первая строка, элементы со второго):", b[0, 1:])

print("\nЗадание 2")
print(f"Сумма a (NumPy): {np.sum(a)}, Среднее: {np.mean(a)}")
list_a = [10, 20, 30, 40, 50, 60]
print(f"Сумма list (Python): {sum(list_a)}")
# Вывод: NumPy требует меньше кода и работает быстрее на больших объемах.

print("\nЗадание 3")
print("Сумма по столбцам (axis=0):", np.sum(b, axis=0))
print("Сумма по строкам (axis=1):", np.sum(b, axis=1))

print("\nЗадание 4")
c = np.array([100, 200, 300])
print("b + c (автоматическое расширение размерности):\n", b + c)

print("\nЗадание 5")
mask = a > 30
print("Маска (a > 30):", mask)
print("Элементы, где a > 30:", a[mask])

print("\nЗадание 6")
unsorted = np.array([5, 2, 9, 1, 7])
print("Отсортированный:", np.sort(unsorted))
print("Индекс максимума:", np.argmax(unsorted))

print("\nЗадание 7")
large_arr_32 = np.arange(10_000_000, dtype=np.int32)
large_arr_64 = np.arange(10_000_000, dtype=np.int64)
large_list = list(range(10_000_000))

print(f"Память int32: {large_arr_32.nbytes / 1024**2:.2f} MB")
print(f"Память int64: {large_arr_64.nbytes / 1024**2:.2f} MB")

start = time.time()
np.sum(large_arr_32)
print(f"Время NumPy: {time.time() - start:.5f} сек")

start = time.time()
sum(large_list)
print(f"Время Python (sum): {time.time() - start:.5f} сек")
