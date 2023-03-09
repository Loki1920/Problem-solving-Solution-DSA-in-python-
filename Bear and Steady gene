from collections import Counter
import sys
import math

n = int(input())
s1 = input()
s = Counter(s1)

if all(e <= n/4 for e in s.values()):
    print(0)
    sys.exit(0)

result = float("inf")
out = 0
for mnum in range(n):
    s[s1[mnum]] -= 1
    while all(e <= n/4 for e in s.values()) and out <= mnum:
        result = min(result, mnum - out + 1)
        s[s1[out]] += 1
        out += 1

print(result)
