dir = {'Fifty Pounds': 50, 'Twenty Pounds': 20, 'Ten Pounds': 10, 'Five Pounds': 5, 'Two Pounds': 2, 'One Pound': 1, 'Fifty Pence': .50,
        'Twenty Pence': .20, 'Ten Pence': .10, 'Five Pence': .05, 'Two Pence': .02, 'One Pence': .01}

ans = list()
pp = float(input())
ch = float(input())
x = ch - pp

if x < 0 :
    print('ERROR')
    quit()

if x == 0:
    print('Zero')
    quit()

a = 0
while a <=x:
    for key in dir:
        if (a + dir[key]) <= x:
            a = a + dir[key]
            if a - x== 0:
                ans.append(key)
                print(ans)
                quit()
            ans.append(key)
            break
print(ans)
#getting change at the counter
