from itertools import combinations_with_replacement

s ,k = input().split()
s = sorted(s)
k = int(k)

from itertools import combinations_with_replacement
c = list(combinations_with_replacement(s,k))
for i in c:
    print(''.join(i))