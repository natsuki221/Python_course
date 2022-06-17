from random import randint as rd
from random import choices

def lottoGen(num):
    
    lotto_list = []
    while len(lotto_list) != 6:
        prize_num = rd(1, num)
        if prize_num not in lotto_list:
            lotto_list.append(prize_num)
        
        
    lotto_list = sorted(lotto_list)
    
    return lotto_list

#print(lottoGen(48))