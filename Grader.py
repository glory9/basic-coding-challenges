#get score
score = input("Enter score:")
#in case of text entry
try:
    s = float(score)
except:
    print("Please enter numeric value between 0.0-1.0.")
    quit()
#to determine grade
if s<0.0:
    print("Error!")
    quit()
elif s>1.0:
    print("Error!")
    quit()
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
else:
    print("F")
