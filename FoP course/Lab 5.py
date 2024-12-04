"""
In a file named password.py, implement a program in Python that prompts
the user to enter a password and then uses a user-defined function and for loop to
check whether or not the password is good. We will define a good password to be a
one that is at least 8 characters long and contains at least one uppercase letter,
at least one lowercase letter, at least one number, and at least one special character
from !@#$%*&?~+.
Example:
    Input: ZSICCnAzfz&A6b+^
    Output: 'That is a good password.'
    Input: IDhF*97BFyS&4hPq
    Output: 'That is a good password.'
    Input: 8vhvdbvgxu3pzhh8
    Output: 'That is not a good password.'
    Input: qwerty
    Output: 'That is not a good password.'
"""
#   add your code here

def checkPassword(password):
    count = 0
    count_upper = 0
    count_lower = 0
    count_number = 0
    special_chars = 0
    if len(password) >= 8:
        count = 1
    for i in password:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i in "!@#$%*&?~+":
            special_chars += 1
        elif i.isdigit():
            count_number += 1
    if count != 0 and count_upper != 0 and count_lower != 0 and count_number != 0 and special_chars != 0:
        return 'That is a good password.'
    else:
        return 'That is not a good password.'



    # complete the function



def main():
    p = input("Enter a password: ")
    print(checkPassword(p))
    # complete the function



# Call the main function if the file has not been imported
if __name__ == "__main__":
  main()














# """
# In a file named isPrime.py, implement a program in Python that prompts
# the user to enter an integer number and then uses user-defined functions
# and for loop to display a message indicating whether or not it is prime.
# Example:
#     Input: 5
#     Output: '5 is prime.'
#     Input: 10
#     Output: '10 is not prime.'
# Hint:
#     A prime number is an integer greater than one that is only divisible by
#     one and itself.
# """
#
#
# #   add your code here
#
# def isPrime(n):
#     """ This function determines whether or not its parameter is prime,
#         returning True if it is, and False otherwise."""
#     #   complete the function
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def main():
#     """ This function determines if a number entered by the user is prime.
#         This function calls the function isPrime(n)."""
#
#     value = int(input("Enter an integer: "))
#     if isPrime(value):
#         print(f"{value} is prime.")
#     else:
#         print(f"{value} is not prime.")
#     # complete the function
#
#
# # Call the main function if the file has not been imported
# if __name__ == "__main__":
#     main()
#






# n = int(input())
#
# def odd_squares(n):
#     odd = 0
#     even = 0
#     for i in range(n):
#         if i % 2 != 0:
#             odd += i
#         else:
#             even += i
#     return even, odd
# print(*odd_squares(n))






# m, n = map(int, input().split())
#
# def odd_squares(m, n):
#     result = 0
#     for i in range(m, n):
#             if i % 2 != 0:
#                 result = result + (i ** 2)
#     return result
# print(m, n, odd_squares(m, n))







# inp = str(input())
#
# def count(a):
#     count_C = 0
#     count_L = 0
#     for i in a:
#         if i.isupper():
#             count_C += 1
#         elif i == ' ':
#             count_L += 1
#     return count_C, count_L
# print(*count(inp))











# """
# In a file named spaces_removed.py, implement a program in Python that prompts
# the user to enter a string and then uses a user-defined function and for loop to
# return the string but with its spaces removed.
# Example:
#     Input: 'Hello World!'
#     Output: 'HelloWorld!'
#     Input: ' a b c d e '
#     Output: 'abcde'
# """
# #   add your code here
#
# lst = list(input())
#
# def no_space(lst):
#     new_lst = []
#     for i in lst:
#         if i != " ":
#             new_lst.append(i)
#     return new_lst
#
# print("".join(no_space(lst)))