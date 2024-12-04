t = int(input())


def sum_of_squares(x):
    if x >= 0:
        return x * (x + 1) * (2 * x + 1) // 6
    else:
        return 0

for _ in range(t):
    n, k = map(int, input().split())
    if k > n:
        print("NO")
        continue

    total = sum_of_squares(n) - sum_of_squares(n - k)

    if total % 2 == 0:
        print("YES")
    else:
        print("NO")

    # lst = [1 if i % 2 == 0 else 0 for i in range(n)]
    # lst = lst[n-k:]
    # ans = sum(lst)
    # print(lst)
    # if ans % 2 == 0:
    #     print("YES")
    # else:
    #     print("NO")