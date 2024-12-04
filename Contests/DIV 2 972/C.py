n, m = map(int, input().split())
lst = []

for i in range(n):
    lst.append(input())

line = "".join(lst)
print(line)
indexes = []
cycle = 0
ind = 0
for i in line:
    narek = ["n", "a", "r", "e", "k"]
    if i == narek[ind % 5]:
        indexes.append(cycle)
        ind += 1
    cycle += 1
indexes = indexes[:len(indexes) - (len(indexes) % 5)]
