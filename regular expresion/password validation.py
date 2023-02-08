import re

print("""Has minimum 8 characters 
--------------------------------
At least one uppercase English letter.
At least one lowercase English letter.
At least one digit.
At least one special character""")
str1=input("Enter the password :")
passw="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
if re.match(passw,str1):
    print("------validated-------")
else:
    print("---------try another password--------")