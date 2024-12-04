# n, k = map(int, input().split())
# if k == 0:
#     print(0)
#     exit(0)
# k_list = list(map(int, input().split()))
# ans = 0
# prev = 0
# crosswalks = 2 ** k
# cycle = 1
# for i in k_list:
#     dist = i - prev
#     ans += (dist * (crosswalks / cycle))
#     prev = i
#     cycle *= 2
# if k_list:
#     ans += (n - k_list[-1])
# print(int(ans))

def solve():
    n, k = map(int, input().split())
    k_list = list(map(int, input().split())) if k > 0 else []

    if k == 0:
        print(n)
        return

    ans = 0
    ind = 0
    for i in range(1, n+1):
        ans += 1
        if ind < k and i == k_list[ind]:
            ind += 1
            ans *= 2


    print(ans)
solve()
