import numpy as np
import math as m

theta1 = m.radians(0.0)
theta2 = m.radians(0.0)
theta3 = m.radians(0.0)

Z = 362.3 # max extension at Z = 162.3 >> meaning that Z stroke is maximum 200mm
a1 = 409
a2 = 380 # length of link 1
a3 = 240 # length of link 2
a4 = 266.2
a5 = 219.5
d = a1+a5-a4-Z

#homogeneous transformation
H0_1 = [[m.cos(theta1), -m.sin(theta1)*m.cos(m.radians(0)), m.sin(theta1)*m.sin(m.radians(0)), a2*m.cos(theta1)],
       [m.sin(theta1), m.cos(theta1)*m.cos(m.radians(0)), -m.cos(theta1)*m.sin(m.radians(0)), a2*m.sin(theta1)],
       [0, m.sin(m.radians(0)), m.cos(m.radians(0)), a1],
       [0,0,0,1]]
#homogeneous transformation
H1_2 = [[m.cos(theta2), -m.sin(theta2)*m.cos(m.radians(180)), m.sin(theta2)*m.sin(m.radians(180)), a3*m.cos(theta2)],
       [m.sin(theta2), m.cos(theta2)*m.cos(m.radians(180)), -m.cos(theta2)*m.sin(m.radians(180)), a3*m.sin(theta2)],
       [0, m.sin(m.radians(180)), m.cos(m.radians(180)), a5],
       [0,0,0,1]]
#homogeneous transformation
H2_3 = [[m.cos(m.radians(0)), -m.sin(m.radians(0))*m.cos(m.radians(0)), m.sin(m.radians(0))*m.sin(m.radians(0)), 0],
       [m.sin(m.radians(0)), m.cos(m.radians(0))*m.cos(m.radians(0)), -m.cos(m.radians(0))*m.sin(m.radians(0)), 0],
       [0, m.sin(m.radians(0)), m.cos(m.radians(0)), a4 + a1 + a5 - Z],
       [0,0,0,1]]
#homogeneous transformation
H3_4 = [[m.cos(theta3), -m.sin(theta3)*m.cos(m.radians(0)), m.sin(theta3)*m.sin(m.radians(0)), 0],
       [m.sin(theta3), m.cos(theta3)*m.cos(m.radians(0)), -m.cos(theta3)*m.sin(m.radians(0)), 0],
       [0, m.sin(m.radians(0)), m.cos(m.radians(0)), 0],
       [0,0,0,1]]

H0_2 = np.dot(H0_1, H1_2)
H2_4 = np.dot(H2_3, H3_4)
H0_4 = np.dot(H0_2, H2_4)

print(np.matrix(H0_4))
print(" ")
print( "d = d" , d)