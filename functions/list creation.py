start=int(input("enter the starting position"))
end=int(input("enter the end position"))

def EvenNums(a,b):
    v=[]
    for i in range(a,b,2):
        v.append(i)
    return v
print(EvenNums(start,end))

