from sympy import log, sin, cos, tan, E, pi, lambdify, diff, sqrt
from sympy.abc import x

# Variables
continuous_function: str      # continuous function
xi: float   # initial guess
max_iterations: int
precision: float

# Get input
print("== Newton-Raphson Method ==")
print()
print("Enter the continuous function:")
continuous_function = input("y = ")
xi = float(input("Enter the initial value: "))
max_iterations = int(input("Max number of iterations: "))
precision = float(input("Precision (10e<-x>): "))

f = lambdify(x, continuous_function)
# Calculating the derivative
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
        print(f"Raiz = {round(xi, 7)}")
        break
    xi = xii
