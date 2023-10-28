from sympy import log, sin, cos, tan, lambdify, E, pi, sqrt
from sympy.abc import x
from bolzano_theorem import BolzanoTheorem

# Variables
continuous_function: str
a: float      # beginning of the interval
b: float      # end of the interval
c: float      # middle of the interval
max_iterations: int
precision: float
bolzano: BolzanoTheorem

# Get input
print("== Bisection Method ==")
print()
print("For ln(), use log().")
print("For log, use log(x, base).")
print("Enter the continuous function:")
continuous_function = input("y = ")
a = float(input("Enter the beginning of the interval: "))
b = float(input("Enter the end of the interval: "))
max_iterations = int(input("Enter the maximum number of iterations: "))
precision = float(input("Enter the precision (10e<-x>): "))
print()

# Processing and output
bolzano = BolzanoTheorem(continuous_function, str(a), str(b))

if not bolzano.calc():  # there is not a zero within the interval
    exit(0)

for i in range(max_iterations):
    print(f"== {i} ==")
    f = lambdify(x, continuous_function)
    fa = f(a)
    fb = f(b)

    # If a root was found
    if fa == 0:
        print(f"The root is: {a}")
        break
    if fb == 0:
        print(f"The root is: {b}")
        break

    c = (a + b) / 2.0
    fc = f(c)

    if (fc == 0.0) or (abs(fc) < precision):
        print(f"The root is: {c}")
        break

    print(f"a = {round(a, 7)}")
    print(f"b = {round(b, 7)}")
    print(f"c = {round(c, 7)}")
    print(f"f(c) = {round(fc, 7)}")
    print()
    print()

    if fc * fa >= 0:
        a = c
    else:
        b = c
