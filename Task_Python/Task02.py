# **Задача 6:** Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых 
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – 
# счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая 
# проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


n = 385916
first = n // 1000
second = n % 1000

first_one = first % 10
first_two = first % 100 // 10
first_free = first // 100

second_one = second // 100
second_two = second % 100 // 10
second_free = second % 10

sum_first = first_one + first_two + first_free
sum_second = second_one + second_two + second_free

if sum_first == sum_second:
    print(f"{n} -> yes")
else:
    print(f"{n} -> no")