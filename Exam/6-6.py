def Recursive(n):
    
    if n == 1:
        return 1
    else:
        return Recursive(n-1) + n

n = int(input('Please enter the value N: '))
for i in range(1, n+1):
    if i == 1:
        print(i,end='')
    else:
        print('+', i,end='',sep='')
print('為', Recursive(n),sep='')