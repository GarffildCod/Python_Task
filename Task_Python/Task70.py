# Задача 6. Собачьи бега

# В собачьих бегах участвует N собак, 
# у каждой из них есть определённое количество очков за сезон. 
# На огромном табло выводятся очки каждой собаки. Однако при выводе 
# был обнаружен баг: собаки с наибольшим и наименьшим количеством очков 
# поменялись местами! Нужно это исправить.

# Дан список очков из N собак. Напишите программу, которая меняет местами 
# наибольший и наименьший элементы в списке.

list_number = [6, 3, 2, 5, 4]
tem = list_number[0]
for i in range(len(list_number)):
    for j in range(len(list_number) - 1):
        if list_number[j] > list_number[j + 1]:
            tem = list_number[j]
            list_number[j] = list_number[j + 1]
            list_number[j + 1] = tem

print(list_number)