word = str(input())
cycle = 0
hello = ["h", "e", "l", "l", "o"]
ans = 0
for letter in word:
    if letter == hello[cycle]:
        ans += 1
        cycle += 1
    cycle = cycle % 5
if ans >= 5:
    print("YES")
else:
    print("NO")