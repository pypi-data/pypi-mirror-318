def prog5():
    print('''
import numpy as np
# Define the function f(x, y)
def func(x, y):
    return x**2 + y**2
# Compute Jacobian (first derivatives)
def compute_jacobian(x, y):
    df_dx = 2 * x  # ∂f/∂x
    df_dy = 2 * y  # ∂f/∂y
    return np.array([df_dx, df_dy])
# Compute Hessian (second derivatives)
def compute_hessian(x, y):
    d2f_dx2 = 2  # ∂²f/∂x²
    d2f_dy2 = 2  # ∂²f/∂y²
    d2f_dxdy = 0  # ∂²f/∂x∂y
    d2f_dydx = 0  # ∂²f/∂y∂x
    return np.array([[d2f_dx2, d2f_dxdy],
                     [d2f_dydx, d2f_dy2]])
# Example values
x_val, y_val = 1.0, 2.0
# Compute Jacobian and Hessian
jacobian = compute_jacobian(x_val, y_val)
hessian = compute_hessian(x_val, y_val)
print("Jacobian:", jacobian)
print("Hessian:\n", hessian)''')