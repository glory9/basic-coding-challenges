name = input("Enter file:")
if len(name) < 1 : name = "regex17.txt"
import re
handle=open(name)
num=re.findall('[0-9]+',handle.read())
numm=list()
for val in num:
    vall=int(val)
    numm.append(vall)
addd=sum(numm)
print(addd)
#file-shortsum.py is a shorter version of this code
