num = int(input())


for i in range(num):
    n = int(input())
    if n % 4 == 0:
        print("YES")
        lst_even = []
        lst_odd = []
        for j in range(1, int(n / 2) + 1):
            lst_even.append(j * 2)
            lst_odd.append(j * 2 - 1)
        lst_odd[-1] = lst_odd[-1] + int(n / 2)
        print(*lst_even, *lst_odd)
    else:
        print("NO")