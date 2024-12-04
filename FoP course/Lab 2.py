x, y = map(float, input().split())

def area(x, y):
    return (x * y) / 43560
print(area(x, y))

x = int(input())
def num(x):
    return x * (x + 1) / 2
print(num(x))


x, y, z = map(float, input().split())

def minmax(x, y, z):
    return min(x, y, z), (x + y + z) - min(x, y, z) - max(x, y, z), max(x, y, z)
print(minmax(x, y, z))

x, y = map(str, input().split())

def swap(x, y):
    lst = [y, x]
    return " ".join(lst)
print(swap(x, y))

name = str(input())

def greet(name):
    return f"Hello {name}"
print(greet(name))

c = float(input())

def CelsiusToFahrenheit(c):
    return c * 1.8 + 32
print(c, CelsiusToFahrenheit(c))

from math import pi

r = float(input())
def areaofacircle(r):
    return pi * r * r
def volumeofasphere(r):
    return r ** 3 * (4/3) * pi
print(areaofacircle(r), volumeofasphere(r))
