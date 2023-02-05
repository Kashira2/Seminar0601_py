# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num1 = float(input('Введите число: '))
# num1 = str(num1)
# num1 = num1.split('.')

# num2 = str(num1[0]) + str(num1[1])
# num2 = int(num2)
# sum = int(0)
# while num2 // 10 > 0:
#     sum += num2 % 10
#     num2 = num2 // 10

# print(sum + (num2 % 10))

def solution(num1):
    res = list(x for x in num1)
    res = list(map(int, num1))
    result = 0
    for i in range(len(res)):
        result = result + res[i]
    return result


num1 = 34,132
num1 = str(num1)
if num1.find(',') != -1:
    num1 = num1.replace('(', '').replace(')', '').replace(',', '').replace(' ', '')
    print(solution(num1))
else:
    print(solution(num1))