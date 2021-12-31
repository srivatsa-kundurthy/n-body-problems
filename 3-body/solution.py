import numpy as np
import matplotlib.pyplot as plt

# CONSTANTS
G = 6.67 * (10**-11)
m1 = 100000
m2 = 500000
m3 = 200000

# INITIAL CONDITIONS
x_1_0 = 400
y_1_0 = 1000

x_2_0 = -3540
y_2_0 = 700

x_3_0 = 3000
y_3_0 = 400

x_1_dot_0 = 0
y_1_dot_0 = 0

x_2_dot_0 = 0
y_2_dot_0 = 0

x_3_dot_0 = 0
y_3_dot_0 = 0

#DATA
x_1_data = [x_1_0]
y_1_data = [y_1_0]
x_2_data = [x_2_0]
y_2_data = [y_2_0]
x_3_data = [x_3_0]
y_3_data = [y_3_0]

x = [x_1_0, x_2_0, x_3_0, x_1_0]
y = [y_1_0, y_2_0, y_3_0, y_1_0]
plt.figure(1)
#plt.plot(x, y)
plt.scatter(x,y)
plt.show()
#distance formulas

def get_r12(x1, x2, y1, y2):
    eq = np.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return eq

def get_r13(x1, x3, y1, y3):
    eq = np.sqrt(((x3 - x1)**2) + ((y3 - y1)**2))
    return eq

def get_r23(x2, x3, y2, y3):
    eq = np.sqrt(((x3 - x2)**2) + ((y3 - y2)**2))
    return eq


# ODES
# r
def get_r1_double_dot(r1, r2, r3):
    eq = (-G * m2 * (r1 - r2)/(np.abs(r1 - r2))**3) - (G * m3 * (r1 - r3)/(np.abs(r1-r3))**3)
    return eq

def get_r2_double_dot(r1,r2,r3):
    eq = (-G * m1 * (r2 - r1) / (np.abs(r2 - r1))**3) - (G * m3 * (r2 - r3) / (np.abs(r2 - r3))**3)
    return eq

def get_r3_double_dot(r1,r2,r3):
    eq = (-G * m1 * (r3 - r1) / (np.abs(r3 - r1))**3) - (G * m2 * (r3 - r2) / (np.abs(r3 - r2))**3)
    return eq

# m1
def get_x1_double_dot(x1,x2,x3,r12,r13):
    eq = (G * m2 * (x1 - x2)/(r12)**3) + (G * m3 * (x1 - x3)/(np.abs(r13))**3)
    return eq

def get_y1_double_dot(y1,y2,y3,r12,r13):
    eq = (G * m2 * (y1 - y2)/(r12)**3) + (G * m3 * (y1 - y3)/(np.abs(r13))**3)
    return eq

# m2
def get_x2_double_dot(x1,x2,x3,r12,r23):
    eq = (G * m1 * (x2 - x1) / (np.abs(r12)) ** 3) + (G * m3 * (x2 - x3) / (np.abs(r23)) ** 3)
    return eq

def get_y2_double_dot(y1,y2,y3,r12,r23):
    eq = (G * m1 * (y2 - y1) / (np.abs(r12)) ** 3) + (G * m3 * (y2 - y3) / (np.abs(r23)) ** 3)
    return eq

#m3
def get_x3_double_dot(x1,x2,x3,r13,r23):
    eq = (G * m1 * (x3 - x1) / (np.abs(r13)) ** 3) + (G * m2 * (x3 - x2) / (np.abs(r23)) ** 3)
    return eq

def get_y3_double_dot(y1,y2,y3,r13,r23):
    eq = (G * m1 * (y3 - y1) / (np.abs(r13)) ** 3) + (G * m2 * (y3 - y2) / (np.abs(r23)) ** 3)
    return eq

def update_position(t):
    dt = 0.1
    x_1 = x_1_0
    y_1 = y_1_0
    x_2 = x_2_0
    y_2 = y_2_0
    x_3 = x_3_0
    y_3 = y_3_0

    x_1_dot = x_1_dot_0
    y_1_dot = y_1_dot_0
    x_2_dot = x_2_dot_0
    y_2_dot = y_2_dot_0
    x_3_dot = x_3_dot_0
    y_3_dot = y_3_dot_0


    for time in np.arange(0, t, dt):
        r12 = get_r12(x_1,x_2, y_1, y_2)
        r13 = get_r13(x_1, x_3, y_1, y_3)
        r23 = get_r23(x_2, x_3, y_2, y_3)

        x_1_double_dot = get_x1_double_dot(x_1,x_2,x_3,r12,r13)
        y_1_double_dot = get_y1_double_dot(y_1,y_2,y_3, r12,r13)

        x_2_double_dot = get_x2_double_dot(x_1, x_2, x_3, r12, r23)
        y_2_double_dot = get_y2_double_dot(y_1, y_2, y_3, r12, r23)

        x_3_double_dot = get_x3_double_dot(x_1, x_2, x_3, r13, r23)
        y_3_double_dot = get_y3_double_dot(y_1, y_2, y_3, r13, r23)

        x_1_dot += x_1_double_dot * dt
        y_1_dot += y_1_double_dot * dt

        x_2_dot += x_2_double_dot * dt
        y_2_dot += y_2_double_dot * dt

        x_3_dot += x_3_double_dot * dt
        y_3_dot += y_3_double_dot * dt


        x_1 += x_1_dot * dt
        y_1 += y_1_dot * dt

        x_2 += x_2_dot * dt
        y_2 += y_2_dot * dt

        x_3 += x_3_dot * dt
        y_3 += y_3_dot * dt
        '''
        x_1 += x_1_double_dot * (dt)**2
        y_1 += y_1_double_dot * (dt)**2

        x_2 += x_2_double_dot * (dt)**2
        y_2 += y_2_double_dot * (dt)**2

        x_3 += x_3_double_dot * (dt)**2
        y_3 += y_3_double_dot * (dt)**2
        '''
        x_1_data.append(x_1)
        y_1_data.append(y_1)
        x_2_data.append(x_2)
        y_2_data.append(y_2)
        x_3_data.append(x_3)
        y_3_data.append(y_3)
    return [x_1, x_2, x_3, y_1, y_2, y_3]
plt.figure(2)
res = update_position(1000)
print(res)
x = res[0:3]
print('x',x)
y = res[3:]
print('y', y)
plt.plot(x_1_data, y_1_data)
#plt.plot(x_2_data, y_2_data)
#plt.plot(x_3_data, y_3_data)
#print(x_1_data)
plt.show()
print('r12', get_r12(x_1_0, x_2_0, y_1_0, y_2_0))