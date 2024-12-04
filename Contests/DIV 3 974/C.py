n = int(input())

for i in range(n):
    num = int(input())
    lst = list(map(int, input().split()))
    mid = num // 2 + 1
    lst.sort()
    if num == 1 or num == 2:
        print(-1)
    else:
        max_mid = max(lst[:mid])
        ans = max_mid * 2 * num + 1 - sum(lst)
        if ans > 0:
            print(ans)
        else:
            print(0)