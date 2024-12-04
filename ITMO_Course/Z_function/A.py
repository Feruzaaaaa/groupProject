t = int(input())

def is_palindrome(word):
    return word == word[::-1]

for i in range(t):
    word = list(str(input()))
    cycle = 0
    if is_palindrome(word):
        print(len(word))
    else:
        for j in range(len(word)):
            if is_palindrome(word[:cycle]):
                answer = word[:cycle]
            cycle += 1
        print(len(answer))

