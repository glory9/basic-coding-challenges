#finding superior subarrays 

c = input().split(',')

d = [int(_) for _ in c]

k = 0
b = list()
while True:
    try:
        a =[d[k],d[k+ 1],d[k + 2],d[k + 3]]
        b.append(a)
        k = k + 1
    except:
        break

f = 0
for _ in b[0]:
    if _ == b[1][f]:
        f = f + 1
        continue
    elif _ > b[1][f]:
        print(b[0])
        break
    else:
        print(b[1])
        break

#c = input().split()
#n = c[1]
#d = c[0].split(',')
