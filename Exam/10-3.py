import csv
import re
from nbformat import write

from sqlalchemy import true

poem = open('/Users/lintzujeng/Documents/GitHub/Python_course/Exam/poem.txt', 'rt', encoding='utf-8')

s = str(poem.read())
s = re.findall('\w', s)
#print(s)

poem.close()


s_dict = {}
for i in range(len(s)):
    if s[i] not in s_dict:
        s_dict[s[i]] = 1
    elif s[i] in s_dict:
        s_dict[s[i]] += 1

s_dict = sorted(s_dict.items(), key=lambda x:x[1], reverse=1)

print(s_dict)
        
        
    

with open ('output.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(s_dict)
    fout.close()