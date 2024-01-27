# Задача 4. Гугл

# Программисты постоянно гуглят ошибки и ищут 
# уже готовый код, который можно использовать для своей программы, 
# чтобы не изобретать велосипед. Андрей поступил также и нашёл для своего проекта код, 
# который должен находить минимальное и максимальное числа в списке. Вот этот код:

# nums_list = []
# N = int(input('Кол-во чисел в списке: '))for _ in range(N):
#  num = int(input('Очередное число: '))
#  nums_list.append(num)
#  
# maximum = 0
# minimum = -1for i in nums_list:
#  if maximum < i:
#    maximum = i
#  if minimum > i:
#    minimum = i
#  print('Максимальное число в списке:', maximum)print('Минимальное число в списке:', minimum)

# Однако он столкнулся с проблемой. Если брать, 
# к примеру, количество чисел 5, то на тестах -1 -2 -3 -4 -5 и 1 2 3 4 5 
# программа выводит неверный результат.

# Доработайте программу так, чтобы она выводила верный результат. 
# Подсказка: для отладки используйте точки останова.


from random import randint

def rand_number(num):
    set_num = []
    for i in range(num):
        num = randint(1, 15)
        set_num.append(num)
    return set_num

def min_max(set):
    maximum = set[0]
    minimum = set[0]
    for i in set:
        if minimum > i:
            minimum = i
        if maximum < i:
            maximum = i
    print(f'Максимальное число в списке: {maximum}, Минимальное число в списке: {minimum}')


def sort_bubble(arr):
    for i in range(in_nam - 1):
        for j in range(in_nam - i - 1):
            if arr[j] > arr[j + 1]:
                puff = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = puff
    

in_nam = int(input("Введите количество: "))
rest_set = rand_number(in_nam)
print(rest_set)
min_max(rest_set)
sort_bubble(rest_set)
print(rest_set)