# **Задача 2:** Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

b = 123
third = b % 10
second = b % 100 // 10
first = b // 100
res = first + second + third
print(f"{b} -> {res} ({first} + {second} + {third})")