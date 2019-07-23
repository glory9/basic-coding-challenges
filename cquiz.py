while True :
    t = input("your number")
    if t == 'done':
        quit()
    try:
        n = int(t)
    except :
        print('wrong value')
        continue
    x = 0
    while x < 3*n :
        y= (x*x) - (n*n)
        print (y)
        x = x + 1
