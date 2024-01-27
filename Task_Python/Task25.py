# **Задача 8. Замечательные числа**

# Что нужно сделать

# Напишите программу, которая находит и выводит все двузначные числа, 
# которые равны утроенному произведению своих цифр. К таким относятся, например, 15 и 24.


numOne = int(input("Enter the firt number - "))
numTwo = int(input("Enter the second number - "))

for i in range(numOne, numTwo):
    n1= i // 10
    n2 = i % 10 
    if n1 * n2 * 3 == i:
        print(i)