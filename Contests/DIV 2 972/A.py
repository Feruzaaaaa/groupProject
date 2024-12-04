num = int(input())
for i in range(num):
    n = int(input())
    lst = ["a", "e", "i", "o", "u"]
    if n < len(lst) or n == len(lst):
        print("".join(lst[:n]))
    else:
        times = n // 5
        rem = n % 5
        A = "a" * times
        B = "e" * times
        C = "i" * times
        D = "o" * times
        E = "u" * times
        if rem == 1:
            print(A + "a" + B + C + D + E)
        elif rem == 2:
            print(A + "a" + B + "e" + C + D + E)
        elif rem == 3:
            print(A + "a" + B + "e" + C + "i" + D + E)
        elif rem == 4:
            print(A + "a" + B + "e" + C + "i" + D + "o" + E)
        else:
            print(A + B + C + D + E)