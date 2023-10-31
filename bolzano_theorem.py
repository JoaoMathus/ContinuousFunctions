from sympy import log, sin, cos, tan, lambdify, E, pi
from sympy.abc import x


class BolzanoTheorem:
    def __init__(self, cont_func: str, a: str, b: str):
        self.continuous_function = cont_func
        self.begin_interval = a
        self.end_interval = b

    def calc(self) -> bool:
        print(f"Intervalo: [{self.begin_interval}, {self.end_interval}]")
        print()

        f = lambdify(x, self.continuous_function)
        fa = f(float(self.begin_interval))
        fb = f(float(self.end_interval))

        print(f"f({self.begin_interval}) = {fa}")
        print(f"f({self.end_interval}) = {fb}")
        if (fa * fb < 0) or (fa == 0) or (fb == 0):
            print("Ha raiz nesse intervalo.")
            return True
        else:
            print("Nao ha raiz nesse intervalo.")
            return False
