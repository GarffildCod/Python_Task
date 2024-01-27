# **Задача 4. Число наоборот**

# Что нужно сделать

# Вводится последовательность чисел, которая оканчивается нулём. 
# Реализуйте функцию, которая принимает в качестве аргумента каждое число, 
# переворачивает его и выводит на экран.

# **Пример**:

# Введите число: 1234
# Число наоборот: 4321

# Введите число: 1000
# Число наоборот: 0001

# Введите число: 0
# Программа завершена!


def revers(num):
    n_list = list(num)
    n_list.reverse()
    n2 = "".join(n_list)
    return n2

n = int(input("Введите число: "))
if n > 0:
    x = revers(n)
    print(f'Число наоборот: {x}')
else:
    print('Некоретный ввод!')