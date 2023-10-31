from sympy import log, sin, cos, tan, E, pi, lambdify, diff, sqrt
from sympy.abc import x

# Variables
continuous_function: str      # continuous function
xi: float   # initial guess
max_iterations: int
precision: float

# Get input
print("== Metodo Newton-Raphson ==")
print()
print("Para ln(), use log().")
print("Para log(), use log(x, base).")
print("Digite a funcao continua:")
continuous_function = input("y = ")
xi = float(input("Digite o valor inicial: "))
max_iterations = int(input("Digite o numero maximo de iteracoes: "))
precision = float(input("Digite a precisao (10e<-x>): "))

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
        print("Foi encontrada uma raiz!")
        print(f"Raiz = {round(xi, 7)}")
        break
    xi = xii
