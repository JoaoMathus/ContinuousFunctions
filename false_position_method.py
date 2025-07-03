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
print("== False Position Method  ==")
print()
print("To use ln(), type log().")
print("To use log(), type log(x, base).")
print("Enter the continuous function:")
continuous_function = input("y = ")
a = float(input("Enter the beginning of the interval: "))
b = float(input("Enter the end of the interval: "))
max_iterations = int(input("Enter maximum iterations number: "))
precision = float(input("Enter the precision (10e<-x>): "))

f = lambdify(x, continuous_function)
if not bolzano_theorem(f, a, b):
    exit(0)

for i in range(max_iterations):
    print(f"== {i} ==")
    fa = f(a)
    fb = f(b)

    if fa == 0.0:
        print(f"Root = {a}")
        break
    if fb == 0.0:
        print(f"Root = {b}")
        break

    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)

    print(f"a    = {round(a, 7)}")
    print(f"f(a) = {round(fa, 7)}")
    print(f"b    = {round(b, 7)}")
    print(f"f(b) = {round(fb, 7)}")
    print(f"c    = {round(c, 7)}")
    print(f"f(c) = {round(fc, 7)}")
    print()

    if (fc == 0) or (abs(fc) < precision):
        print(f"Root = {round(c, 7)}")
        break

    if fa * fc >= 0.0:
        a = c
    else:
        b = c
