from math import sin, radians
g = 9.81
# velocity = int(input("Enter velocity in m/s: "))
# angle = radians(int(input("Enter angle in degrees: ")))
def height(angle, velocity):
    return ((velocity * sin(angle)) ** 2) / (g * 2)
def n_range(angle, velocity):
    return ((velocity ** 2) * (sin(angle * 2)))/g
def time(angle, velocity):
    return (2 * velocity * sin(angle))/g
# for i in range(1, 10):
#     angle = radians(i * 10)
#     print("angle: ", i * 10)
#     print("Range = ", round(n_range(angle, velocity), 3))
#     print("Height = ", round(height(angle, velocity), 3))
#     print("Time = ", round(time(angle, velocity), 3))
#     print("----------------")
# angle = int(input("Enter angle in degrees: "))
# print("Angle: ", angle)
# print("Range = ", round(n_range(radians(angle), velocity), 3))
# print("Height = ", round(height(radians(angle), velocity), 3))
# print("Time = ", round(time(radians(angle), 3.1), 3))
def error(theoretical, actual):
    print(round((abs(theoretical - actual)/theoretical) * 100, 3), "%")
theoretical = []
measured = [0.148, 0.29, 0.29, 0.347, 0.42, 0.42, 0.525, 0.729, 0.69]
for i in range(1, 10):
    theoretical.append(round(time(radians(i * 10), 3.1), 3))
cycle = 0
print(len(theoretical), len(measured))
for value in measured:
    error(theoretical[cycle], value)
    cycle += 1




#
#
# students_grades = {"Kairat": 85, "Asylbek": 78, "Emir": 52, "Aidar": 88, "Amal": 10}
#
# def get_student_grade(name):
#     if name in students_grades:
#         return f"{name}'s grade is: {students_grades[name]}"
#     else:
#         return f"Student {name} not found."
#
# def add_student_grade(name, grade):
#     students_grades[name] = grade
#     return f"Added {name} with a grade of {grade}."
#
# print(get_student_grade("Kairat"))
# print(get_student_grade("Alim"))
#
# print(add_student_grade("Alim", 75))
# print(get_student_grade("Alim"))




# LIMIT_AGE = 18
# def laws(age):
#     if age >= LIMIT_AGE:
#         smoking = 0
#         driving = 0
#     else:
#         smoking = LIMIT_AGE - age
#         driving = (LIMIT_AGE - 1) - age
#     return [smoking, driving]
# age = int(input())
# data = laws(age)
# print("You can smoke after ", data[0], " years")
# print("You can drive after ", data[1], " years")
#
# num = 11692013098647223345629478661730264157247460343808
# print(len(str(num)))
# cycle = 0
# while num >= 2:
#     cycle += 1
#     print(num, "cycle: ", cycle)
#     num /= 2
#
#
# strin = "string is value"
#
# for i in lst:
#     if i == 4:
#         print(i, "is 4")
#         if i == 4:
#             print(i, "is 4, hello")
#     elif i == 5:
#         print(i, "is 5")
#         if i == 5:
#             print(i, "is 5, hello")
# import module_emirgay
# from module_emirgay import imgay, emir
#
#
# emir("Джусик")
# print(imgay + " " + imgay)
#
#
# for i in range(2):
#     num = int(input("Enter a number: "))
#     assert is_even(num) == True
#     print(num, "is even")
