from random import randint as rd

def recieptGen():
    
    prize_list = []
    for i in range(8):
        
        prize_list.append(str(rd(0, 9)))
    prize_str = ''.join(prize_list)
    
    return prize_str

#print(recieptGen())    
    