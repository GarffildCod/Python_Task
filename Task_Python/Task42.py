# **Задача 6. Письмо**

# Что нужно сделать

# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое не помещается в конверт. Напишите программу, которая подскажет, сколько раз нужно сложить письмо пополам, чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.

# Советы и рекомендации

# Обратите внимание, что лист квадратный.

# Принимаем, что лист размером 12х12 свободно входит в конверт 12х12.
n = int(input('Введите размер письма - '))
c = 0
while n > 12:
    n = n / 2
    c = c + 2
print(c)