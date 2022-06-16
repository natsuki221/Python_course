def NGenerator(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
        yield sum

n = int(input('請輸入N值？'))
done = True
while done:
    if n < 0:
        print('輸入錯誤，請重新輸入')
        n = int(input('請輸入N值？'))
    else:
        done = False   
        #print(NGenerator(n))
        for i in NGenerator(n):
            print(i)