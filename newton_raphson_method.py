from sympy import log, sin, cos, tan, lambdify, diff
from sympy.abc import x

# Variables
continuous_function: str      # continuous function
xi: float   # initial guess
max_iterations: int
precision: float

# Get input
print("== Newton-Raphson Method ==")
print()
print("For ln(), use log().")
print("For log, use log(x, base).")
print("Enter the continuous function:")
continuous_function = input("y = ")
xi = float(input("Enter the initial guess: "))
max_iterations = int(input("Enter the maximum number of iterations: "))
precision = float(input("Enter the precision (10e<-x>): "))

# Processing and output

# Turning the function from input into a python function
f = lambdify(x, continuous_function)
# Calculating the derivative and turning into a python function
df = lambdify(x, eval("diff(continuous_function, x)"))

print(f"f(x)  = {continuous_function}")
print(f"df(x) = {diff(continuous_function, x)}")

for i in range(max_iterations):
    f_xi = f(xi)
    df_xi = df(xi)

    xii = xi - (f_xi / df_xi)
    f_xii = f(xii)
    df_xii = df(xii)

    print()
    print(f"== {i} ==")
    print(f"xi      = {round(xi, 7)}")
    print(f"f(xi)   = {round(f_xi, 7)}")
    print(f"df(xi)  = {round(df_xi, 7)}")
    print(f"xii     = {round(xii, 7)}")
    print(f"f(xii)  = {round(f_xii, 7)}")
    print(f"df(xii) = {round(df_xii, 7)}")

    if (f_xi == 0.0) or (abs(f_xi) < precision):
        print("A root was found!")
        print(f"Root = {round(xi, 7)}")
        break
    xi = xii
