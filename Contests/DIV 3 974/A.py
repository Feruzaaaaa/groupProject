n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    new_lst = []
    cycle = 0
    balance = 0
    ans = 0
    for j in lst:
        if j >= b:
            new_lst.append(0)
            balance += j
        elif j == 0 and balance != 0:
            new_lst.append(1)
            balance -= 1
            ans += 1
        else:
            new_lst.append(j)

        cycle += 1
    print(ans)