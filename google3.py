#comparing smaller strings and counting the result
import re

b = input().split()
a = b[0].split(',')
d = b[1].split(',')

g = list()
for _ in a:
    x = min(_)
    c = re.findall(x,_)
    g.append(len(c))

e = 0
h = list()
for _ in d:
    y = min(_)
    z = re.findall(y,_)
    h.append(len(z))
j = list()
for _ in h:
    m = 0
    f = 0
    for v in g:
        if _ > g[f]:
            m = m + 1
        f = f + 1
    j.append(m)

print(j)
