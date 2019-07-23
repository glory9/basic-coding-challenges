def countingValleys(n, s):
    a = 0
    b = 0
    c = 0
    d = 0
    mount = 0
    valley = 0
    egg = list()
    for letter in s:
        if letter == 'U':
            a = a + 1
        elif letter == 'D':
            b = b + 1
        c = c + 1
        if a == b and (a+b) > 1:
            f = s[d:c]
            egg.append(f)
            a = 0
            b = 0
            d = c
    for g in egg:
        if g.startswith('U'):
            mount = mount + 1
        elif g.startswith('D'):
            valley = valley + 1
    return valley
n = int(input('n'))
s = input('s').rstrip()
res = countingValleys(n,s)
print(res)
