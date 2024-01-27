# Задача 5. Кратность

# Пользователь вводит список из N 
# чисел и число K. Напишите код, выводящий на экран сумму 
# индексов элементов списка, которые кратны K.

# Пример:

# Кол-во чисел в списке: 4

# Введите 1 число: 1

# Введите 2 число: 20

# Введите 3 число: 30

# Введите 4 число: 4

# Сумма индексов: 4

# Введите делитель: 10

# Индекс числа 20: 1

# Индекс числа 30: 2

# Сумма индексов: 3


num_list = []
col_num = int(input('Кол-во чисел в списке: '))
for i in range(col_num):
    step_num = int(input(f'Введите {i + 1} число:'))
    num_list.append(step_num)

sum_index = 0
for i in range(len(num_list) + 1):
    sum_index += i
print(f'Сумма индексов: {sum_index}')

del_id = int(input('Введите делитель: '))

sum_index = 0
for i in range(len(num_list)):
    if num_list[i] % del_id == 0:
        print(f'Индекс числа {num_list[i]}: {i}')
        sum_index += i
print(f"Сумма индексов: {sum_index}")