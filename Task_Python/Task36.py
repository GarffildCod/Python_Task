# Задача 8. Прятки 2

# Пока все прятались, “голя” решил схитрить и считать секунды быстрее, чем нужно.

# Напишите программу, которая выводит только чётные числа в порядке убывания 
# от N до 1 включительно, 
# используя цикл for. Нельзя использовать условный оператор.
num = int(input("Ведите количество - "))

for i in range(num, 0 , - 2):
    print(i)