t = int(input())

for i in range(t):
    x, y, k = map(int, input().split())
    num1 = (abs(x - y) // k) * 2
    