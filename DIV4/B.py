t = int(input())

for i in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        row = str(input())
        lst.append(row.index("#") + 1)
    lst.reverse()
    lst_final = " ".join(map(str, lst))
    print(lst_final)