# **Задача 9. ...Теперь можно посчитать и свою**

# Что нужно сделать

# Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, 
# а не зря ли она работает столько времени на одном месте? Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.

# Пользователь вводит десять чисел. Напишите программу, которая проверяет,
# упорядочены ли они по возрастанию.


nd = [5, 2, 5, 4, 5, 54, 7, 34 , 9, 123, 11]
countUp = 0
countDoun = 0

for i in range(len(nd) - 1):
    if nd[i] < nd[i + 1]:
        countUp += 1
    else:
        countDoun += 1

if countUp > countDoun:
    print("UP")
else:
    print("Doun")