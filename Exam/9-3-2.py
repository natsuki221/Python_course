import re

poem_str = '白日依山盡，黃河入海流。欲窮千里目，更上一層樓。'

print(poem_str)

ans = re.match('白日', poem_str)
if ans:
    print(ans.group())
else:
   print('NOT FOUND')

ans = re.match('一層', poem_str)
if ans:
    print(ans.group())
else:
    print('NOT FOUND')

ans = re.match('.*一層', poem_str)
if ans:
    print(ans.group())
else:
    print('NOT FOUND')
    
ans = re.search('一層', poem_str)
if ans:
    print(ans.group())
else:
    print('NOT FOUND')

ans = re.findall('一層', poem_str)
if ans:
    print(ans)
else:
    print('NOT FOUND')
    
ans = re.split('，', poem_str)
if ans:
    print(ans)
    
ans = re.sub('。', '；', poem_str)
if ans:
    print(ans)