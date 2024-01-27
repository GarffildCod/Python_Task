# **Задача 6. Успеваемость в классе**

# Что нужно сделать

# В классе N человек. Каждый из них получил за урок по информатике оценку: 
# 3, 4 или 5, двоек сегодня не было. Напишите программу, 
# которая получает список оценок — N чисел — и выводит на экран сообщение 
# о том, кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.


import random

array = []
numFree = 0
numFour = 0
numFive = 0

for i in range(20):
    item = random.randint(2, 5)
    array.append(item)

for i in range(len(array)):
    if array[i] < 4:
        numFree += 1
    elif array[i] < 5:
        numFour += 1
    else:
        numFive += 1

print(f"Количество троечников равна {numFree} \nКоличество хорошистов равна {numFour} \nКоличесво отличников равна {numFive}")