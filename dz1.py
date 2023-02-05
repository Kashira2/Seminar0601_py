# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num1 = int(input('Введите число, которое нужно перевести в двоичную систему: '))

binary_number = []
while num1 // 2 > 0 :
    binary_number.append(num1 % 2)
    num1 = num1 // 2 
binary_number.append((num1*2) // 2)

# for i in range(len(binary_number)):
#     print(binary_number[len(binary_number) - i - 1], end='')

res = [print(binary_number[len(binary_number) - i - 1], end='') for i in range(len(binary_number)) ]