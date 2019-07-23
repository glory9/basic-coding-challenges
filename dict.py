#Use mbox-short.txt as file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

adrs = dict()
count = 0
for line in handle :
    if not line.startswith('From ') : continue
    line = line.split()
    man = line[1]
    adrs[man] = adrs.get(man,0) + 1

bigman = None
bigfreq = 0
for man,freq in adrs.items() :
    if freq > bigfreq :
        bigman = man
        bigfreq = freq
print(bigman,bigfreq)
#prints person with most emails sent and the number of emails
