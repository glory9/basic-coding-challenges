import re

def jumpingOnClouds(c):
    print(re.findall('$[1]([0]+)',c))
    if re.search('$[1]([0]+)',c) : #and (len(re.findall('$10+',c)))%2 != 0:
        k = c[:len(c)-1]
        print('yes')
    elif not '1' in c and ((len(c))%2) == 0:
        k = c[:len(c)-1]
        print('j', round(len(c)/2))
        quit()
    else:
        k = c
    l = k[0]
    x = 0
    a = 0
    while k.find(l,x) < (len(k) - 1):
        if k[k.find(l,x) + 2] == '1':
            l = k[(k.find(l,x) + 1)]
            x = x + 1
        else:
            l = k[k.find(l,x) + 2]
            x = x + 2
        a = a + 1
        #print(a)
    if re.search('$10+',c) and (len(re.findall('$10+',c)))%2 != 0:
        return a + 1
    else:
        return a #jump_count
n = int(input())
c = input().rstrip()
res = jumpingOnClouds(c)
print(res)
