num = int(input())

for k in range(num):
    length = int(input())
    matrix = list(input())
    n = length**0.5

    def divide_list(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    if n == round(n):
        n = int(n)
        square = [['1' if i == 0 or j == 0 or i == n-1 or j == n-1 else '0' for j in range(n)] for i in range(n)]
        if square == divide_list(matrix, n):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')