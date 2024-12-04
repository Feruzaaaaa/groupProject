def max_knowledge(n, a):
    if n == 0:
        return 0, ""
    if n == 1:
        return a[0], "O"

    dp = [0] * n
    meditated = [""] * n

    dp[0] = a[0]
    meditated[0] = "O"

    if a[1] > 2 * a[1]:
        dp[1] = a[0] + a[1]
        meditated[1] = "O"
    else:
        dp[1] = 2 * a[1]
        meditated[1] = "M"

    for i in range(2, n):
        if dp[i - 1] + a[i] > dp[i - 2] + 2 * a[i]:
            dp[i] = dp[i - 1] + a[i]
            meditated[i] = "O"
        else:
            dp[i] = dp[i - 2] + 2 * a[i]
            meditated[i] = "M"
            meditated[i - 1] = "O"  # Устанавливаем, что перед предыдущей лекцией не медитировали

    return dp[n - 1], meditated


# Пример использования:
n = int(input("Введите количество лекций: "))
a = list(map(int, input("Введите количество знаний для каждой лекции: ").split()))
result, meditations = max_knowledge(n, a)
print(result)
print("".join(meditations))
