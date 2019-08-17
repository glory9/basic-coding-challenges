#finding the fairest possible division into two sets

a = input().split(',')
b = sorted([int(_) for _ in a])

g = list()
h = list()

g.append(b[len(b) - 1])
b.remove(b[len(b) - 1])
v = abs(sum(b) - sum(g))
h.append(v)

x = 0
while x <= (len(b)/2) - 1:
    g.append(b[len(b) - 2])
    b.remove(b[len(b) - 2])
    k = abs(sum(b) - sum(g))
    h.append(k)
    x = x + 1

print(min(h))
