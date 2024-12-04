num = int(input())

for i in range(num):
    n, k = map(int, input().split())
    res_list = list(map(int, input().split()))
    kraken = True
    for j in range(k):
        if kraken:
            if res_list == []:
                break
            else:
                first = res_list[0]
                res_list.remove(res_list[0])
                if (first - 1) != 0:
                    res_list.insert(0, first - 1)
                kraken = False
        else:
            if res_list == []:
                break
            else:
                last = res_list[-1]
                res_list.remove(res_list[-1])
                if (last - 1) != 0:
                    res_list.append(last - 1)
                kraken = True
    print(n - len(res_list))