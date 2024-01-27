# **Задача 2. Очень простая задача**

# У вас есть список numbers. Напишите программу, 
# которая заполняет список числами от 0 до 100 и выводит его на экран.


import random

input_nam = int(input('Введите числа: '))
f = []
for _ in range(input_nam):
    f.append(random.randint(1, 10))

print(f)

