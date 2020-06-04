from sympy import *
from math import *
init_printing(use_unicode = False, wrap_line = False)
x = Symbol('x')
y = Symbol('y')

print("IVP solver using picard theorem")
print("Example list:")

def f1(x, y):
    return x**2 + y + 1
print("1. y' = x**2 + y + 1")

def f2(x, y):
    return x*y
print("2. y' = x*y")

def f3(x, y):
    return 1 + y**2
print("3. y' = 1 + y**2")

def f4(x, y):
    return x / 2 * y - x * y
print("4. y' = x / 2 * y - x * y")

print("***        Choose an option!        ***")
op = int(input())

dic = {1:f1, 2:f2, 3:f3, 4:f4}

print("Enter numeric x0 and y0 which y(x0) = y0")
print("x0 = ", end = '')
x0 = int(input())
print("y0 = ", end = '')
y0 = int(input())
print()
yList = [y0]
for i in range(5):
    yList.append(y0 + integrate(dic[op](x, yList[i]), (x, x0, x)))
    print("y" + str(i + 1) + ' = ' + str(yList[i + 1]))
    print()

print("By: Mahdi Amiri Shavaki :)")
print("Thank you for running my program ^_^")
preventionFromTermination = input()
