res1 = '2+2'
res2 = '-2+3*2-6/2'
res3 = '6/2-2'
res = res2.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')
res = res.split()
print(res)

count = res.count('/') + res.count('*')
print(count)
j = 0
for i in range(len(res)-1):
    while j != count:    
        if res[i] == '*':
            print(res)
            res[i - 1] = str(int(res[i-1]) * int(res[i+1]))
            res = res[:i] + res[i+2:]
            print(res)
            j += 1
        elif res[i] == '/':
            res[i - 1] = str(int(res[i-1]) // int(res[i+1]))
            res = res[:i] + res[i+2:]
            print(res)
            j += 1
        


        