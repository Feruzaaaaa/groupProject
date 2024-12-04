checker = int(input("1 for loop, 2 while loop "))
n = int(input("Enter number of iterations "))

if checker == 1:
    for k in range(n):
        print(k, "By using for loop ")
elif checker == 2:
    k = 0
    while k < n:
        print(k, "By using while loop ")
        k += 1
