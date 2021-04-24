# -*- coding: utf-8 -*-

import math as m

print("Start....")

omega = float(input("Rotation Angle omega:")) 
phi = float(input("Rotation Angle phi:")) 
kappa = float(input("Rotation Angle kappa:")) 

mx = float(input("Scaling in X:")) 
my = float(input("Scaling in Y:"))

tx = float(input("Translation Tx:")) 
ty = float(input("Translation Ty:")) 
tz = float(input("Translation Tz:")) 

omega = m.radians(omega)
kappa = m.radians(kappa)
phi = m.radians(phi)

print(" ")

# Rotation Matrix

r11 = m.cos(phi)*m.cos(kappa)
r12 = -m.cos(phi)*m.sin(kappa)
r13 = m.sin(phi)

r21 = m.cos(omega)*m.sin(kappa) +  m.cos(kappa)*m.sin(omega)*m.sin(phi)
r22 = m.cos(kappa)*m.cos(omega) - m.sin(phi)*m.sin(kappa)*m.sin(omega)
r23 = -m.cos(phi)*m.sin(omega) 

r31 = m.sin(kappa)*m.sin(omega) - m.sin(phi)*m.cos(kappa)*m.cos(omega)
r32 = m.cos(kappa)*m.sin(omega) + m.sin(phi)*m.sin(kappa)*m.cos(omega)
r33 = m.cos(omega)*m.cos(phi)

# Foward 
a1_f_p = mx*r11/(r33 + tz)
b1_f_p = my*r21/(r33 + tz)
a2_f_p = mx*r12/(r33 + tz)
b2_f_p = my*r22/(r33 + tz)
a0_f_p = (mx*r13 + tx)/(r33 + tz)
b0_f_p = (my*r23 + ty)/(r33 + tz)
c1_f_p = r31/(r33 + tz)
c2_f_p = r32/(r33 + tz)

    
print(" ")
print("--- Projective Foward Result ----")
print("a1     //    a2    //  a0")
print(round(a1_f_p, 5) ,"    ",round(a2_f_p, 5),"   ",round(a0_f_p, 5))
print("---------------------------------")
print("b1    //    b2    //  b0")       
print(round(b1_f_p, 5) ,"    ",round(b2_f_p, 5),"   ",round(b0_f_p, 5))
print("---------------------------------")
print("c1    //    c2 ")       
print(round(c1_f_p, 10) ,"    ",round(c2_f_p, 10))

# Backward
Q=a1_f_p*b2_f_p-a2_f_p*b1_f_p
a0_b_p = (a2_f_p * b0_f_p - a0_f_p * b2_f_p)/Q
b0_b_p = (a0_f_p * b1_f_p - a1_f_p * b0_f_p)/Q

a2_b_p = (a0_f_p * c2_f_p - a2_f_p)/Q 
b2_b_p = (a1_f_p - a0_f_p * c1_f_p)/Q

a1_b_p = (b2_f_p - b0_f_p * c2_f_p)/Q
b1_b_p = (c1_f_p * b0_f_p - b1_f_p)/Q

c1_b_p = (c2_f_p * b1_f_p - c1_f_p * b2_f_p)/Q
c2_b_p = (a2_f_p * c1_f_p - a1_f_p * c2_f_p)/Q


print("--- Projective Backward Result ----")
print("a1_b     //    a2_b    //  a0_b")
print(round(a1_b_p, 5) ,"    ",round(a2_b_p, 5),"   ",round(a0_b_p, 5))
print("-----------------------------------")
print("b1_b    //    b2_b    //  b0_b")       
print(round(b1_b_p, 5) ,"    ",round(b2_b_p, 5),"   ",round(b0_b_p, 5))
print("-----------------------------------")
print("c1_b    //    c2_b ")       
print(round(c1_b_p, 20) ,"    ",round(c2_b_p, 20))










































