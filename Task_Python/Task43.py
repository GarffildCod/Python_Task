# **Задача 7. Стипендия**

# Что нужно сделать

# Ежемесячная стипендия студента составляет educational_grant рублей, 
# а расходы на проживание превышают стипендию и составляют expenses рублей в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Составьте 
# программу расчёта суммы денег, которую необходимо получить у родителей один раз в 
# начале обучения, чтобы можно было прожить учебный год (десять месяцев), используя 
# только эти деньги и стипендию.

# **Пример**:

# Введите стипендию: 10000

# Введите расходы на проживание: 13000

# У родителей необходимо попросить 49030.431

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
sum_home = (expenses*10) + (((expenses*3)/100)*10)
sum_step = educational_grant * 10

vopros = sum_home - sum_step

print(vopros)