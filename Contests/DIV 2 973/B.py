num = int(input())


for i in range(num):
    lng = int(input())
    lst = list(map(int, input().split()))
    while lng > 2:
        frs = lst[-2]
        scd = lst[-3]
        lst.pop(-2)
        lst.pop(-2)
        lst.insert(-1, frs - scd)
        lng -= 1
    ans = lst[-1] - lst[0]
    print(ans)