# **Задача 4. С заботой о природе**

# Что нужно сделать

# Огромный заповедник поделён на большое количество секторов. Все сектора пронумерованы. Вы устроились на работу лесничим и отвечаете за группу секторов с номерами 30–35.

# В ваши обязанности входит:

# - следить за тем, чтобы посетителей в каждом секторе было не больше десяти;
# - фиксировать количество нарушений этого правила.

# Напишите программу, которая для каждого сектора запрашивает текущее количество людей в нём, и если оно больше десяти, то фиксирует нарушение. В конце выведите количество нарушений.

# Пример:

# Людей в 30-м секторе: 7

# Всё спокойно.

# Людей в 31-м секторе: 11

# Нарушение! Слишком много людей в секторе!

# Людей в 32-м секторе: 100

# Нарушение! Слишком много людей в секторе!

# Людей в 33-м секторе: 10

# Всё спокойно.

# Людей в 34-м секторе: 0

# Всё спокойно.

# Людей в 35-м секторе: 1

# Всё спокойно.

# Количество нарушений: 2

from random import randint
array = []
arrSec = [30, 31, 32, 33, 34, 35]
stop = 0

for i in range(5):
    item = randint(0, 15)
    array.append(item)

for i in range(len(array)):
    if array[i] <= 10:
        print(f'В секторе {arrSec[i]} находится {array[i]} - Все хорошо')
    else:
        print(f'В секторе {arrSec[i]} находится {array[i]} - Все плохо')
        stop += 1
    f = input("Что бы проверить следующий сектор нажмити ENTER")

print(f"Нарушений выявлено {stop}")