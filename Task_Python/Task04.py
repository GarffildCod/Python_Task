# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


coll = int(input("Количество монет - "))
falg = 0
eagle = 0
for i in range(coll):
    nam = int(input('Введите сторону(0 - орел/1 - герб) - '))
    if nam == 0:
        eagle += 1
    elif nam == 1:
        falg += 1
if eagle < falg:
    print(f'Переверните орлов {eagle}')
else:
    print(f"Переверните гербы {falg}")