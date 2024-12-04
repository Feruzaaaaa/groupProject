"""
An amusement park sets different entry fees based on the visitors' ages:
- Entry for childern aged less then 5 years: Free entry.
- Entry for childern aged 5-13 years: $10.00.
- Entry for seniors aged 60 years and above: $15.00.
- Entry for all other ages: $30.00.

In a file named park.py, implement a program in Python that prompts the
user to enter the ages of all of the visitors in a group, one age per line.
A blank line indicates that there are no more visitors in the group.
The program should uses a while loop to calculate the total entry cost for
the group with an appropriate message. Use decimals when displaying the cost.

Example:
    Input:
        Enter the age of the guest (blank to finish): 3
        Enter the age of the guest (blank to finish): 5
        Enter the age of the guest (blank to finish): 10
        Enter the age of the guest (blank to finish): 10
        Enter the age of the guest (blank to finish): 25
        Enter the age of the guest (blank to finish): 19
        Enter the age of the guest (blank to finish):
    Output:
        The total cost for the group is $90.00
"""

  # add your code here

def cost():
    line = input()
    total = 0
    while line != "":
        n = int(line)
        if n >= 5 and n < 13:
            total += 10
        elif int(n) > 60:
            total += 15
        elif int(n) < 5:
            total += 0
        else:
            total += 30
        line = input()
    return total



def main():
    print(cost())

# Call the main function if the file has not been imported
if __name__ == "__main__":
  main()





# def is_palindrome(string):
#     cycle = 0
#     while cycle < (len(string)/2):
#         if string[cycle] == string[-(cycle + 1)]:
#             cycle += 1
#             continue
#         else:
#             return False
#     return True
# print(is_palindrome("kaitiak"))
