num = int(input())

lst = list(map(int, input().split()))
minim = 0
ans = 0
for i in lst:
    ans += i
    if ans < 0:
        minim += abs(ans)
        ans = 0
print(minim)



# if lst[0] < 0:
#     negative = 0
#     for i in lst:
#         if i < 0:
#             negative += i
#         else:
#             break
#     print(abs(lst[0]))
# elif lst[0] > 0 and lst[1] < 0:
#     print(abs(lst[1]) - lst[0])
# else:
#     if sum(lst) >= 0:
#         print(0)
#     elif sum(lst) < 0:
#         print(abs(sum(lst)))