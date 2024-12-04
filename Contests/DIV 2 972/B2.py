inp = int(input())

for i in range(inp):
    n, m, q = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()
    david = list(map(int, input().split()))
    for j in david:
        if j < b[0]:
            print(b[0] - 1)
        elif j > b[-1]:
            print(n - b[-1])
        else:
            l, r = 0, len(b) - 1
            while l < r:
                mid = (l + r + 1) // 2
                if b[mid] > j:
                    r = mid - 1
                else:
                    l = mid
            mid = abs(b[l] - b[l+1]) // 2
            print(mid)