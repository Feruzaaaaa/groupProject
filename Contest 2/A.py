num = int(input())
result = 0

def isodd(num):
    if num % 2 == 0:
        return False
    else:
        return True

for i in range(num):
    n, a, b = map(int, input().split())
    if (2 * a) <= b:
        result = n * a
    else:
        if isodd(n):
            result = (n // 2) * b + a
        else:
            result = int((n / 2) * b)
    print(result)