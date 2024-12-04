n, t = map(int, input().split())
lst = list(map(int, input().split()))
book = 0
cycle = 0
for i in range(n):
    if book > t:
        break
    book += lst[cycle]
    cycle += 1
print(book)