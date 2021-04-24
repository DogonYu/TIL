# 구현 - 단어 뒤집기 2

import sys
import re

txt = sys.stdin.readline().strip()
result = []
if '<' in txt:
    txt = re.findall('<?[a-z 0-9]+>?', txt)
    for x in txt:
        if '<' in x:
            result.append(x)
        else:
            t = x.split(' ')
            result.append(' '.join([y[::-1] for y in t]))
    print(''.join(result))
else:
    print(' '.join([x[::-1] for x in txt.split(' ')]))