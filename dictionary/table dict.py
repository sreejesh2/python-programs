dic1 = {1: ["sreejesh", 23, 'pala'],
         2: ["pavan", 23, 'kannur'],
         3: ["anand", 24, 'wayanad'],
         }


print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'PLACE'))


for key, value in dic1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))