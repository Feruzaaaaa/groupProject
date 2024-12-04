num = int(input())

for i in range(num):
    result = 0
    cycle = 0
    item = int(input())
    inputs = input().split()
    for j in inputs:
        if cycle % 2 == 0:
            result += int(j)
        else:
            result -= int(j)
        cycle = cycle + 1
    print(result)