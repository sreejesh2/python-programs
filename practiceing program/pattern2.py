"""
Piramid pattern
      *
    * * *
  * * * * *
* * * * * * *
"""






num = int(input("enter a number"))

for i in range(num):
    print("  "*(num-i)+"* "*(2*i+1))