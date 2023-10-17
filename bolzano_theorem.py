from sympy import log, sin, cos, tan, lambdify
from sympy.abc import x
from math import e, pi


class BolzanoTheorem:
    def __init__(self, cont_func: str, a: str, b: str):
        self.continuous_function = cont_func
        self.begin_interval = a
        self.end_interval = b

    def calc(self) -> bool:
        print(f"Interval: [{self.begin_interval}, {self.end_interval}]")
        print()

        f = lambdify(x, self.continuous_function)
        fa = f(float(self.begin_interval))
        fb = f(float(self.end_interval))

        print(f"f({self.begin_interval}) = {fa}")
        print(f"f({self.end_interval}) = {fb}")
        if (fa * fb < 0) or (fa == 0) or (fb == 0):
            print("There is a zero within this interval")
            return True
        else:
            print("There is not a zero within this interval")
            return False
