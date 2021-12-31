import numpy as np

# initial conditions
cm = 0 #m
m1 = 5 #kg
m2 = 5 #kg
G = 6.67 * 10**-11 #N kg^2/m^2


R_0 = 1 #m
R_dot_0 = 0 #m


def compute_R_double_dot(m1, m2, G, R):
    eq = G * (m1 + m2)/(R**2)
    return eq

# equations

def r1(cm, m1, m2, R):
    eq = cm + (m2 * R)/(m1 + m2)
    return eq


def r2(cm, m1, m2, R):
    eq = cm - (m2 * R)/(m1 + m2)
    return eq

def R(t):
    dt = 0.001 #s
    R = R_0
    R_dot = R_dot_0

    for time in np.arange(0, t, dt):
        R_double_dot = compute_R_double_dot(m1, m2, G, R)


        R_dot += R_double_dot * dt

        R += R_dot * dt
    return R

def R_alt(t):
    eq = (G * (m1 + m2) * (t**2)/2)**(1/3)
    return eq

print(R(1))
print(R_alt(1))

