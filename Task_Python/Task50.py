# **Задача 9. Поел - можно и поспать, поспал - можно и поесть**

# У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью, 
# но засыпает всегда до того, как наступит полночь, обычно в 23 часа. 
# А ещё он очень любит поесть. Он ест каждый час и если съедает больше 2000 калорий, 
# то он просто падает спать. Напишите программу, которая поможет Саше понять, 
# всё ли с ним хорошо. 
# Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.

noslip = int(input('Введите когда вы проснулись - '))
sum_calori = 0
for i in range(noslip, 24):
    sum_calori += 2000
    print(f'{i}')
print(sum_calori)