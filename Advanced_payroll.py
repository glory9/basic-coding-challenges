hours = input("Enter hours:")
rate = input("Enter pay rate:")
try:
    h = float(hours)
    r = float(rate)
except:
    print("Please enter numeric value.")
    quit()
def computepay(h,r):
    if h<=40:
        pay= h*r
        return pay
    else:
        reg = h*r
        bonus= (h-40)*(r*0.5)
        pay = reg + bonus
        return pay
print (computepay(h,r))
