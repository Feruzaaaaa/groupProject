"""
In a file named count.py, implement a program in Python that prompts the user
to enter a non negative integer value and then uses a recursive user-defined
function that handles the base case and recursive cases and counts from the
entered value down to zero, then prints a message "Reached the base case.", and
then counts from zero up to the entered value.
Example:
    Input:
        Enter a non negative integer value: 10
    Output:
        10
        9
        8
        7
        6
        5
        4
        3
        2
        1
        0
        Reached the base case.
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
"""

#   add your code here

def count(number, original=None):
    if original is None:
        original = number
    if number == 0:
        print(0)
        print("Reached the base case.")
        number -= 1
        count(number, original)
    elif number < 0:
        if abs(number) == original:
            print(abs(number))
            return
        print(abs(number))
        number -= 1
        count(number, original)
    else:
        print(number)
        number -= 1
        count(number, original)



# def count(n, original=None):
#     # Set the original value on the first call
#     if original is None:
#         original = n
#
#     # Base case: when n reaches zero, print zero and the base case message
#     if n == 0:
#         print(n)
#         print("Reached the base case.")
#         return
#
#     # Print the current value while counting down
#     print(n)
#
#     # Recursive case: count down
#     count(n - 1, original)
#
#     # Print the value while counting up after reaching the base case
#     if n != original:
#         print(n)



def main():
    count(int(input("Enter a non negative integer value: ")))
    #complete the function



# Call the main function if the file has not been imported
if __name__ == "__main__":
  main()





# def all_and_nothing(total=0.0):
#     n = input("Enter values: ")
#     if n == "":
#         return total
#     else:
#         num = float(n)
#         total += num
#     return all_and_nothing(total)
# print(all_and_nothing())