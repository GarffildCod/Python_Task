# **Задача 4. Среднее на отрезке**

# Что нужно сделать

# Напишите программу, которая считывает с клавиатуры два числа a и b, 
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число с: '))
summ = 0
count = 0
for i in range(a, b +1):
    if i % c == 0:
        count += 1
        summ += i
if count == 0:
    print('Расчет невозможен, так как нет подходящих чисел')
else:
    print(summ / count)


