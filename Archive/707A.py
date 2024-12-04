n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(str, input().split())))
for i in matrix:
    for j in i:
        if j != 'W' and j != 'B' and j != "G":
            print("#Color")
            exit(0)
print("#Black&White")