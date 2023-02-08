"""first method"""

#num = input("enter a number")
# n= num[::-1]
# print(n)

"""second method"""
num = int(input("Enter the number"))
reverse = 0
while num != 0:
    current = num % 10
    reverse = 10*reverse
    reverse = reverse+current
    num =num //10
print(reverse)

