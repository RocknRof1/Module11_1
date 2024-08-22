import numpy as np

# Одномерный массив из списка с умножением.
arr = np.array([1, 2, 3, 4, 5])
arr = arr * 2
print(arr)

# Функция mean можно вычислить среднее арифметическое значение.
a = np.array([[1, 2, 3], [4, 5, 6]])
mean_all = a.mean()
print(mean_all)

# Агрегаторы min и max находят минимальное и максимальное значение.
a = np.array([[1, 2, 3], [4, 5, 6]])
min_all = a.min()
max_all = a.max()
print(min_all)
print(max_all)

# двумерный массив, обращение к отдельному элементу.
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a[0, 4])
