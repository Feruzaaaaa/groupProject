num = int(input())

def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

for i in range(num):
    n, k = map(int, input().split())
    res_list = list(map(int, input().split()))
    kraken = True
    if sum_of_list(res_list) <= k:
        print(n)
        continue
    else:
        for j in range(k):
            if kraken:
                first = res_list[0]
                res_list.remove(res_list[0])
                res_list.insert(0, first - 1)
                kraken = False
            else:
                last = res_list[-1]
                res_list.remove(res_list[-1])
                res_list.append(last - 1)
                kraken = True
            print(res_list)
    print(n - len(res_list))