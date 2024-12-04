
n = int(input())

for i in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    if (a1 > b1 and a1 > b2) and (a2 > b1 and a2 > b2):
        print(4)
    elif (a1 > b1 or a1 > b2) and (a2 > b1 or a2 > b2):
        print(2)
    elif (a1 > b1 and a1 < b2) and a2 == b2 or (a2 > b1 and a2 < b2) and a1 == b2:
        print(2)
    else:
        print(0)
