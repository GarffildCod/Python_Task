# **Задача 2. Деление клетки**

# В одной лаборатории наблюдают за одноклеточной амёбой. 
# Мы знаем, что каждые три часа она делится на 2 клетки. 
# Нам нужно для этой лаборатории написать программу, 
# которая будет выводить сколько прошло часов и сколько получилось клеток. 
# Также нас попросили писать на каждом этапе деления сколько осталось часов 
# до завершения наблюдения, чтобы ученым было проще формулировать выводы 
# на определённом этапе наблюдения.

# Пример сообщений:

# Прошло часов: 3.
# Клеток: 2.
# Часов до конца эксперимента: 12
# Прошло часов: 6...


time = 12
cletka = 1 
taim = 0
proslo = 0

for i in range(3, time + 1, 3):
    cletka += 1
    taim = time - i
    proslo += 3
    print(f"Прошло часов: {i}")
    print(f"Клеток: {cletka}")
    print(f"Часов до конца эксперимента: {taim}")
    print(f"Прошло часов: {proslo}...")
    print()