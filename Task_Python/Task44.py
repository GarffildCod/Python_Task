# **Задание 1. Дом для семьи**

# Максим написал программу, которая должна определять, 
# подходит ли земельный участок для его семьи или нет. Живут 
# они втроем, вот и условие будет таким же: если количество квадратных 
# метров делится на 3, то участок подходит.

# For in meters 100,90,95,87,102:
#  if meters % 3 == 1:
#    print(meters, 'Подходит')
#  else:   print(meters, 'Не подходит')

meters = [100, 90, 95, 87, 102]

for i in meters:
    if i % 3 == 1:
        print(i, 'Подходит')
    else:
        print(i, 'Не подходит')