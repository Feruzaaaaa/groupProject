""""Recursion"""
# class Doll():
#     def __init__(self, name, innerDoll):
#         self.name = name
#         self.innerDoll = innerDoll
#         if innerDoll == None:
#             self.HasSeam = False
#         else:
#             self.HasSeam = True
# d1 = Doll("Dimitry", None)
# d2 = Doll("Catherine", d1)
#
# def open_doll(name):
#     print("My name is ", name.name)
#     if name.HasSeam == True:
#         inner = name.innerDoll
#         open_doll(inner)
#     else:
#         print("We opened all dolls!")
#
# d1 = Doll("Catherine", None)
# d2 = Doll("Dimitry", d1)
# d3 = Doll("Victor", d2)
# d4 = Doll("Kate", d3)
#
# open_doll(d3)


# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

# def num_es(s):
#     if s == " ":
#         return 0
#     elif len(s) == 1:
#         return 1 if s[0] == "e" else 0
#     left = num_es(s[0])
#     right = num_es(s[1:])
#     return left + right
# print(num_es("alisher pussy juicy i love you very much"))

# def deblank(s):
#     if s == "":
#         return s
#     elif len(s) == 1:
#         return "" if s[0] == " " else s
#     left = deblank(s[0])
#     right = deblank(s[1:])
#     return left + right
# x = print(deblank("All is her"))