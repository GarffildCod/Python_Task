# **Задача 8. Сумма чисел**

# Напишите программу, где пользователь 
# вводит любые два целых положительных числа. 
# А программа суммирует все числа в диапазоне от первого до второго. 
# Гарантируется, что первое введённое число всегда меньше второго.

# Пример:

# Введите первое число: 5
# Введите второе число: 10
# Сумма чисел от 5 до 10 равна 45 = 5 + 6 +7 + 8 + 9 + 10

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
sumnum = 0
for i in range(num1, num2 + 1):
    sumnum += i
print(f'Сумма чисел от {num1} до {num2} равна {sumnum}')