# **Задача 8. НОД**

# Что нужно сделать

# Напишите функцию, 
# вычисляющую наибольший общий делитель двух чисел.


numOne = int(input("Введите целое число: "))
numTwo = int(input("Введите целое число: "))
count = 0

def namber(num):
    g = []
    for i in range(num - 1, 1, -1):
        if (num % i == 0):
            g.append(i)
    return g

f = namber(numOne)
g = namber(numTwo)

for i in f:
    for j in g:
        if i == j:
            count += i
print(f'Все делители чесла {numOne} - {f}\nВсе делители чесла {numTwo} - {g}')
print(f'Общий делители - {count}')