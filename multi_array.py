#If input values don'y have white space in between, debug with hashed code below.
#su = list()
#for r in arr:
#    for s in r:
#        sub = list()
#        for t in s:
#            sub.append(int(t))
#        su.append(sub)
def hourglassSum(arr):
    a = 0
    c = 0
    d = 0
    e = 0
    i = 0
    yep = list()
    while  e < 4:
        f = 0
        a = 0
        while f < 4:
            b = i + 2
            sum1 = (arr[i][a]) + (arr[i][a + 1]) + (arr[i][a + 2]) + (arr[i + 1][a + 1]) + (arr[b][a]) + (arr[b][a + 1]) + (arr[b][a + 2])
            a = a + 1
            yep.append(sum1)
            f = f + 1
        i = i + 1
        e = e + 1
    return max(yep)

arr = []
for _ in range(6):
    arr.append(list(map(int,input().rstrip().split())))
result = hourglassSum(arr)
print(result)
