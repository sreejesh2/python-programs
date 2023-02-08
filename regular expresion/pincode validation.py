import  re
s=(input("Enter pincode"))
pin="^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$";
p=re.compile(pin)
if re.match(p,s):
    print("--valid--")
else:
    print("--incorrect pincode--")