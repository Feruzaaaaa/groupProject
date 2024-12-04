from math import ceil
num = int(input())

for i in range(num):
    n = int(input())
    x, y = map(int, input().split())
    print(ceil(n/min(x,y)))