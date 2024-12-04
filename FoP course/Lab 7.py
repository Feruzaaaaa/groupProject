"""
In a file named sublists.py, implement a program in Python that prompts the
user to enter as integer the length of a list and then uses two user-defined
functions:
    - The function mylist to create a list of n random positive integer numbers
    having single digits. Use the function mylist to create a list named l.
    - The function sublists(l) that returns all the sublists of the list l.
Example:
    Input:
        Enter the length of the list: 3
    Output:
        The generated list is [8, 7, 2]
        The list of sublists of [8, 7, 2] is
        [[], [8], [7], [2], [8, 7], [7, 2], [8, 7, 2]]
    Input:
        Enter the length of the list: 4
    Output:
        The generated list is [3, 9, 5, 5]
        The list of sublists of [3, 9, 5, 5] is
        [[], [3], [9], [5], [5], [3, 9], [9, 5], [5, 5], [3, 9, 5], [9, 5, 5], [3, 9, 5, 5]]
Hint:
    To generate a random positive number having single digit, use the following commands:
        from random import randint
        randint(0,9)
"""


#   add your code here

def sublists(l):
    """ This function return a list containing all the sublists of the list l.
        Parameter:
            l is the list for which the sublists are generated
    """
    sublists = [[]]
    for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            sublists.append(l[i:j])
    print(sublists)

def mylist(n):
    """ This function generates a list of n random positive integer numbers
    having single digits.
        Parameter:
            n is the length of the list
    """
    from random import randint
    lst = [randint(0,9) for i in range(n)]
    return lst


# Demonstrate the functions mylist and sublists
def main():
    n = int(input("Enter the length of the list: "))
    #   complete the function
    lst = mylist(n)
    sublists(lst)


# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()



# """
# In a file named numlist.py, implement a program in Python that prompts the
# user to enter as integer the length n of a list and then uses two user-defined
# functions:
#     - The function mylist to create a list of n random positive integer numbers
#     having single digits. Use the function mylist to create a list named l.
#     - The function numlist(l, a, b) that counts in the list l the number of values
#     that are greater than some minimum value a and less than some maximum value b.
# Example:
#     Input:
#         Enter the length of the list: 5
#         Enter the minimum value: 3
#         Enter the maximum value: 9
#     Output:
#         The number of values between 3 and 9 in [3, 5, 1, 7, 5] is 3
#     Input:
#         Enter the length of the list: 10
#         Enter the minimum value: 2
#         Enter the maximum value: 7
#     Output:
#         The number of values between 2 and 7 in [1, 8, 1, 4, 6, 8, 2, 8, 7, 6] is 3
# Hint:
#     To generate a random positive number having single digit, use the following commands:
#         from random import randint
#         randint(0,9)
# """
#
# #   add your code here
#
# def numlist(l, a, b):
#     """ This function returns from a list of integers the number of values
#         that are greater than some minimum value and less than some maximum value.
#         Parameters:
#             l is a list
#             a the minimum acceptable value
#             b the maximum acceptable value
#         Precondition:
#             a < b
#     """
#     #   complete the function
#     count = 0
#     for i in l:
#         if i > a and i < b:
#             count += 1
#     print(a, b, l, count)
#
#
#
# def mylist(n):
#     """ This function generates a list of n random positive integer numbers
#     having single digits.
#         Parameter:
#             n is the length of the list
#     """
#     from random import randint
#     #   complete the function
#     lst = [randint(0,9) for i in range(n)]
#     return lst
#
#
# # Demonstrate the functions mylist and numlist
# def main():
#     n = int(input("Enter the length of the list: "))
#     #   complete the function
#     numlist(mylist(n), a, b)
#
# # Call the main function if the file has not been imported
# if __name__ == "__main__":
#   main()