# Use the file name mbox-short.txt as the file name
#error loop for when file name can't be found
x = 1
while x > 0 :
    try :
        fname = input("Enter file name: ")
        fh = open(fname)
        count = 0
        total = 0
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:") : continue
            count = count + 1
            value = line[20: ]
            val = value.rstrip()
            turn= float(val)
            total = total + turn
        mean = total/count
        print("Average spam confidence:",mean)
    except:
        continue
