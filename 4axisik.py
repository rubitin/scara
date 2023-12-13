import numpy as np
import math as m

a1 = 580
a2 = 420

x = 630
y = 650
z = 1170
d = 1293 -z

l = m.sqrt((x+22.5)**2 + (y-22.5)**2)

fi1 = m.atan2((y-22.5),(x+22.5))
fi2 = m.acos((a1**2 + l**2 -a2**2)/(2*a1*l))
fi3 = m.acos((a1**2 + a2**2 -l**2)/(2*a1*a2))

theta1 = fi1+fi2
theta2 = m.radians(180) -fi3

print("Axis 1 =",m.degrees(theta1), "degrees")
print("Axis 2 =",-m.degrees(theta2), "degrees")
print("Z stroke =", d, "mm")