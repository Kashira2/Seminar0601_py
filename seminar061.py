# #######################################################   лист компрейшн

# from random import randint as RI

# my_list = [RI(0, 10) for i in range(10)]

# print(my_list)

# ##########################################################   с условием

# from random import randint as RI

# my_list = [i for i in range(10) if i%2 == 0]

# print(my_list)

# ############################################################   двойной цикл

# my_list = [k + i for k in range(5) for i in range(10)]

# print(my_list)

#############################################################                 map

# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()
# print(string)

# string = list(map(int, string))                    # Выводит строку, как int
# print(string)

#########################################################         еще map   с функцией внутри
# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()

# def cube(x):
#     return x**2

# string = list(map(int, string))
# string = list(map(cube, string))
# print(string)

# ############################################################                  лямда (функция внутри map)


# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()

# string = list(map(int, string))
# string = list(map(lambda x: x**2, string))
# print(string)

# ################################################################                фильтр (условие при котором будет выводится или не выводится)

# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()

# string = list(map(int, string))
# string = list(filter(lambda x: x % 2 == 0, string))
# print(string)


###############################################################           энумирейт (Нумерует )

# string = '1 2 3 45 6 7 8 9 07 457'
# string = string.split()
# for i, item in enumerate(string, 1):    # второе число, то с какого начинается счет
#     print(f'Индекс = {i}, элемент = {item}')

# ########################################################################################      зип

# nums = '1 2 3 4 5 6 7'
# letters = 'a b c d e f g'

# nums = nums.split()
# letters = letters.split()

# new_list = list(zip(nums, letters))

# print(new_list)

##########################################################################################


res1 = '2+2'
res2 = '-2+3*2-6/2'
res3 = '6/2-2'
res = res2.replace(' ', '')
print(res)

# multiplication for function = 1
# division for function = 2
# addition for function = 3
# subtraction for function = 4

def first_move(znak, znak2, res):                           # функция, которая делает чтото в зависимости от знака
    part1 = res[znak-1] + res[znak] + res[znak+1]
    if znak2 == 1:
        part_result = str(int(part1[0]) * int(part1[2]))
        res = res.replace(part1, part_result)
    elif znak2 == 2:
        part_result = str(int(part1[0]) // int(part1[2]))
        res = res.replace(part1, part_result)
    elif znak2 == 3:
        part_result = str(int(part1[0]) + int(part1[2]))
        res = res.replace(part1, part_result)
    else:
        part_result = str(int(part1[0]) - int(part1[2]))
        res = res.replace(part1, part_result)
    return res

if res[0] == '-':                                                                   # Счетчик для определения кол-ва циклов дальше
    count = (res.count('-') - 1) + res.count('+') + res.count('*') + res.count('/')
else:
    count = res.count('-') + res.count('+') + res.count('*') + res.count('/')
    
    print(count)

for i in range(count):
    index_multiplication = res.find('*')   
    index_division = res.find('/')
    if index_multiplication != -1 or index_division != -1:                                      
            if index_multiplication < index_division and not index_multiplication == -1:            # x*x
                index_multiplication = res.find('*')
                res = first_move(index_multiplication, 1, res)
                print(f' умножение прошло: {res}')
                index_multiplication = res.find('*')
                index_division = res.find('/')
            else:                                                                                      # x/x
                index_division = res.find('/')
                res = first_move(index_division, 2, res)
                print(f'деление прошло: {res}')
                index_division = res.find('/')
    else:
        index_addition = res.find('+')
        index_subtraction = res.find('-')
        if res[0] == '-':
            index_subtraction = res.find('-', res.find('-')+1)
            if res[2] == '-':                                                           # -x-x
                part1 = res[index_subtraction-2] + res[index_subtraction-1] + res[index_subtraction] + res[index_subtraction+1]
                part_result = str(int(part1[1]) + int(part1[3]))
                res = res.replace(part1, '-' + part_result)
                print(f'сложение прошло: {res}')
            elif index_addition != -1 and index_addition > index_subtraction and res[index_addition-2] != '-':          # -x-x
                res = first_move(index_addition, 4, res)
                print(f'сложение прошло: {res}')
            elif index_addition != -1 and index_addition > index_subtraction and res[index_addition-2] == '-':         # -x + x      
                part1 = res[index_addition-2] + res[index_addition-1] + res[index_addition] + res[index_addition+1]
                part_result = str(int(part1[3]) - int(part1[1]))
                res = res.replace(part1, part_result)
                print(f'сложение прошло: {res}')
            elif res[index_subtraction-2] == '+' or res[index_subtraction-1] == res[0]:                             # x - x
                res = first_move(index_subtraction, 4, res)
                print(f'вычитание прошло: {res}')
            else:
                part1 = res[index_subtraction-2] + res[index_subtraction-1] + res[index_subtraction] + res[index_subtraction+1]     # -x - x
                part_result = str(int(part1[1]) + int(part1[3]))
                res = res.replace(part1, '-' + part_result)
                print(f'сложение прошло: {res}')
        elif index_addition != -1 and index_addition > index_subtraction and res[index_addition-2] != '-':         # x + x
            res = first_move(index_addition, 3, res)
            print(f'сложение прошло: {res}')
        elif index_addition != -1 and index_addition > index_subtraction and res[index_addition-2] == '-':           #   x - x + x
            part1 = res[index_addition-2] + res[index_addition-1] + res[index_addition] + res[index_addition+1]
            part_result = str(int(part1[3]) - int(part1[1]))
            res = res.replace(part1, part_result)
            print(f'сложение прошло: {res}')
        elif res[index_subtraction-2] == '+' or res[index_subtraction-1] == res[0]:                                   #      x + x 
            res = first_move(index_subtraction, 4, res)
            print(f'вычитание прошло: {res}')
        else:                                                                                                   # x - x - x
            part1 = res[index_subtraction-2] + res[index_subtraction-1] + res[index_subtraction] + res[index_subtraction+1]
            part_result = str(int(part1[1]) + int(part1[3]))
            res = res.replace(part1, '-' + part_result)
            print(f'сложение прошло: {res}')
        


        

print(res)
