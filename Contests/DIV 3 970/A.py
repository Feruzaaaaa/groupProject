num = int(input())
cycle = 0
for i in range(num):
    a, b = map(int, input().split())
    if ((a / 2) + b) % 2 == 0:
        print("YES", "Cycle - 1", cycle)
    elif a != 0 and (a + b * 2) % 2 == 0:
        print("YES", "Cycle - 2", cycle)
    elif (a == 0 and b % 2 == 0) or (b == 0 and a % 2 == 0):
        print("YES", "Cycle - 3", cycle)
    else:
        print("NO", "Cycle - 4", cycle)
    cycle += 1