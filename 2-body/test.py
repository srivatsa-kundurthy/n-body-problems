import numpy as np

# equation dy/dx = x

# solution y = .5x^2

# initial conditions
y0 = 0

def get_dydx(x):
    return x

def y(x):
    dx = 0.00001
    y = y0
    for val in np.arange(0, x, dx):
        dydx = get_dydx(val)
        y += dydx * dx
    return y

def y_general(x):
    return x**2/2

k = 5
print(y(k))
print(y_general(k))
