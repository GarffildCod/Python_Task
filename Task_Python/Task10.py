# **Задача 22:**
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите n:"))
m = int(input("Введите m:"))

def on_set(s):
    list = []
    for i in range(s):
        g = int(input(f"Введите число {i + 1}: "))
        list.append(g)
    sett = set(list)
    return sett

set_n = on_set(n)
set_m = on_set(m)
lok = set_n & set_m
liste = list(lok)
liste.sort
for i in liste:
    print(i, end=' ')