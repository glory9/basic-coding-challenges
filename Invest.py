s = input()
e = s.split(':')

b = e[1].split('|')
p = e[0].split('|')

bm = list()
pf = list()
void = list()
result = list()

for _ in b :
    bc = _.split(',')
    bm.append(bc)
for _ in p :
    po = _.split(',')
    for _ in po:
        void.append(_)
    pf.append(po)

for _ in bm:
    v = 0
    if _[0] and _[1] not in void:
        result.append('BUY,' + _[0] + ',' + _[1] + ',' + str(_[2]))
    while v < len(pf):
        if _[0] and _[1] in pf[v]:
            if _[2] > pf[v][2]:
                result.append('BUY,' + _[0] + ',' + _[1] + ',' + str(int(_[2])-int(pf[v][2])))
            elif _[2] < pf[v][2]:
                result.append('SELL,' + _[0] + ',' + _[1]+ ',' + str(int(pf[v][2]) - int(_[2])))
        v = v + 1
result = sorted(result,reverse=True)
for _ in result:
    print(_)
