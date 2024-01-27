# Задача 6. Простые числа

# Пользователь вводит число N — количество чисел в последовательности. 
# Напишите программу, которая проверяет, 
# сколько из этих чисел являются простыми. Для проверки простоты числа 
# реализуйте функцию isPrime


def isPrime(num):
    ist = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ist.append(i)
    return ist

one = isPrime(9)
two = isPrime(19)
free = isPrime(24)
print(one)
print(two)
print(free)