def subArraySum(arr, n, Sum):
    curr = 0
    m = {}

    for x in range(0,n):
        curr = curr + arr[x]
        if curr == Sum:
            return "True"

        elif (curr - Sum) in m:
            return "True"

        else:
            m[curr] = x
            continue

    return "False"

arr = [2,3,15,1,16]
n = 5
Sum = 8
x = subArraySum(arr, n, Sum)
print(x)
