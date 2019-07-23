text = "X-DSPAM-Confidence:    0.8475";
poi= text.find(':')
num = text[poi+1: ]
num1= num.lstrip()
num2= num1[0:6]
res=float(num2)
print(res)
