#ordering integers in rows/arrays accorrding to magnitude

A = [int(x) for x in input().split(",")]

e = list()
big = list()
big.append(e)

for _ in A:
    if len(e) == 0:
        e.append(_)
        continue

    for each in big:
        if _ < min(each):
            e.append(_)
            break
        else :
            f = list()
            f.append(_)
            big.append(f)
            break

print(len(big))
