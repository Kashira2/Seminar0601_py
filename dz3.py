res1 = '2+2'
res2 = '-8+3*2-6/2'
res3 = '-6/2*3-2'
res = res3.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')
res = res.split()


###################################################### первый счетчик цикла и работа с умножением и деление

count = res.count('/') + res.count('*')       
j = 0
while j != count:       
    for i in range(len(res)-1):
        if res[i] == '*':
            res[i - 1] = str(int(res[i-1]) * int(res[i+1]))
            res = res[:i] + res[i+2:]
            j += 1
            break
        elif res[i] == '/':
            res[i - 1] = str(int(res[i-1]) // int(res[i+1]))
            res = res[:i] + res[i+2:]
            j += 1
            break

############################################################ убираем минус из начала списка

if res[0] == '-': 
    if res[2] == '+':
        res[0] = str(int('-' + res[1]) + int(res[3]))
        res = res[:1] + res[4:]
    elif res[2] == '-':
        res[0] = str(int('-' + res[1]) - int(res[3]))
        res = res[:1] + res[4:]
        
# второй счетчик

if res[0] == '-':                                                 
    count = res.count('+') + res.count('-') - 1
else:
    count = res.count('+') + res.count('-')

################################################### разбираемся с вычитанием и сложением
j = 0
while j != count:
    for i in range(len(res)-1):
        if res[i] == '+':                 
            res[i-1] = str(int(res[i-1]) + int(res[i+1]))
            res = res[:i] + res[i+2:]
            print(f'Убрали плюс {res}')
            j += 1
            break
        elif res[i] == '-':                 
            res[i-1] = str(int(res[i-1]) - int(res[i+1]))
            res = res[:i] + res[i+2:]
            print(f'Убрали минус {res}')
            j += 1
            break

print(int(res[0]))