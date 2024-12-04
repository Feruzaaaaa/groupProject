n = int(input())

lst = list(map(int, input().split()))
mid = sum(lst) // n
min_value = min(lst)
max_value = max(lst)

if min_value == lst[0] and max_value == lst[-1]:
    ans = max_value - min_value

