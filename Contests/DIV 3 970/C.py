start = int(input())
for k in range(start):
    l, r = map(int, input().split())
    numbers = [l]
    difference = 1
    current = l

    while current + difference <= r:
        current += difference
        numbers.append(current)
        difference += 1
    print(len(numbers))

# start = int(input())
# for k in range(start):
#     l, r = map(int, input().split())
#     ans = 0
#     cycle = 0
#     while l + cycle <= r:
#         ans += 1
#         l += cycle
#         cycle += 1
#     print(ans)