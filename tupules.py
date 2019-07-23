#code to find the different times mails were sent and sort them out with their freq
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

adrs = dict()
count = 0
for line in handle :
    if not line.startswith('From ') : continue
    line = line.split()
    pro = line[5]
    pro = pro.split(':')
    tim = pro[0]
    adrs[tim] = adrs.get(tim,0) + 1

dat = sorted(adrs.items())
for k,v in dat[ : ] :
    print(k,v)
