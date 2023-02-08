string = input("enter a string")
done = []
count = 0


def isExist(c):
    for i in done:
        if i == c:
            return False
    return True


for i in string:
    if isExist(i):
        done.append(i)
        for j in string:
            if i == j:
                count += 1
        print(i, ": ", count)
    count = 0
