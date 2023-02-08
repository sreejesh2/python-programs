# it = int(input("enter the number of value"))
# print("enter the numbers")
# l1=[]
# for i in range(it):
#     num = int(input())
#     l1.append(num)
# print(l1)
#
# s=input().strip()
# print(s)
# def count_substring(string, sub_string):
#
#     c = string.upper()
#     if sub_string not in c:
#         count=c.count(sub_string)
#
#     return count
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

    # count = count_substring(string, sub_string)
    # print(count)
# original_string = input()
# substring = input()
# occurrences = original_string.count(substring)
# print(occurrences)
#
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if (string[i:i + len(sub_string)] == sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)