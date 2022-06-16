def Combination(m, n):
    
    if m < n:
        m, n = n, m
        
    if n == 0 or m == n:
        return 1
    
    else:
        return Combination(m-1, n) + Combination(m-1, n-1)
    
    
m = int(input('Please enter value M: '))
n = int(input('Please enter value N: '))
#print(combination(m,n))
print('The result of picking {} from {} is {}'.format(m,n,Combination(m, n)))