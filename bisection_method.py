from sympy import log, sin, cos, tan, lambdify, E, pi, sqrt
from sympy.abc import x
from bolzano_theorem import bolzano_theorem

# Variables
continuous_function: str
a: float      # beginning of the interval
b: float      # end of the interval
c: float      # middle of the interval
max_iterations: int
precision: float

# Get input
print("== Bisection Method  ==")
print()
print("To use ln(), type log().")
print("To use log(), type log(x, base).")
print("Enter a continuous function:")
continuous_function = input("y = ")

# TODO: Change the input of a and b
a = float(input("Enter the beginning of the interval: "))
b = float(input("Enter the end of the interval: "))

max_iterations = int(input("Enter the maximum number of iterations: "))
precision = float(input("Enter the precision (10e<-x>): "))
print()

f = lambdify(x, continuous_function)
if not bolzano_theorem(f, a, b):
    exit(0)

for i in range(max_iterations):
    print(f'== {i} ==')
    fa = f(a)
    fb = f(b)

    if fa == 0:
        print(f'Root = {a}')
        break
    if fb == 0:
        print(f'Root = {b}')
        break

    c = (a + b) / 2.0
    fc = f(c)

    if (fc == 0.0) or (abs(fc) < precision):
        print(f'Root = {c}')
        break

    print(f'a = {round(a, 7)}')
    print(f'b = {round(b, 7)}')
    print(f'c = {round(c, 7)}')
    print(f'f(c) = {round(fc, 7)}')
    print()
    print()

    if fc * fa >= 0:
        a = c
    else:
        b = c
