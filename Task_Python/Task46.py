# **Задача 3. Лотерея 2**

# Напишите программу для немного усложнённой версии задачи про выигрышные билеты. 
# Есть заранее известные номера билетов: 345, 19, 87, 1020 и 421 
# (можете брать свои номера, не стесняйтесь). 
# Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на 5. 
# Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.

number = [345, 19, 87, 1020, 421, 342, 222, 555, 412]
count = 0
for i in number:
    if i < 1000 and i > 99 and i % 5 == 0:
        print(f'Номер выигрышного билета - {i}')
        count += 1
print(f"всего выйграло - {count} билетов")