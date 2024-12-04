w = int(input())
n = int(input())
balance = 0
required = []
getting = []

for i in range(n):
    g, b = map(int, input().split())
    getting.append(g)
    required.append(b)
