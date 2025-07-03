from sympy import log, sin, cos, tan, E, pi, FunctionClass, lambdify
from sympy.abc import x

def bolzano_theorem(cont_func: FunctionClass, begin: float, end: float) -> bool:
    print(f'Interval [{begin}, {end}]')
    print()
    
    fa = cont_func(begin)
    fb = cont_func(end)
    
    print(f'f({begin}) = {fa}')
    print(f'f({end}) = {fb}')
    
    if (fa * fb < 0) or (fa == 0) or (fb == 0):
        print("There's a root within the interval.")
        return True
    else:
        print("There's NOT a root within the interval.")
        return False

if __name__ == '__main__':
    bolzano_theorem(lambdify(x, '10-x**2'), -2.0, 5.0)
