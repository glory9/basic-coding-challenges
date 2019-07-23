big = None
small = None
while True:
    x = input('enter an integer')
    if x == 'done':
        break
    try :
        p = int(x)
    except :
        print ('Invalid input')
        continue
    if big is None:
        big = p
    elif p > big :
        big = p
    if small is None :
        small = p
    elif p < small :
        small = p
print ('Maximum is', big)
print ('Minimun is', small)
y = small * big
print ('ExtremeProduct is', y)
