inp = int(input())

for i in range(inp):
    n, m, q = map(int, input().split())
    b1, b2 = map(int, input().split())
    david = int(input())
    if david < b1 and david < b2:
        print(min(b1, b2) - 1)
    elif david > b1 and david > b2:
        print(n - max(b1, b2))
    else:
        mid = abs(b1 - b2) // 2
        print(mid)