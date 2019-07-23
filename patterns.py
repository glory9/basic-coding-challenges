s = input()
length = len(s)
l = 0
j = s
invest = list()
for _ in range(length - 2):
    t = 3
    while t <= len(j):
        h = j[:t]
        t = t + 1
        if 'A' in h and 'B' in h and 'C' in h:
            invest.append(h)
    l = l + 1
    j = s[l:]
return len(invest)
