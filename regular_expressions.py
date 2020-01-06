name = input("Enter file:")
if len(name) < 1 : name = "regex17.txt"
import re
handle=open(name)
print(sum(int(val) for val in re.findall('[0-9]+',handle.read())))
