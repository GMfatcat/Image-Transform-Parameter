# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:53:34 2021

@author: user
"""


import math as m

print("Start....")


alpha = float(input("Rotation Angle Alpha:")) 
beta = float(input("Shearing Angle beta:")) 
mx = float(input("Scaling in X:")) 
my = float(input("Scaling in Y:"))
a0 = float(input("Translation a0:")) #a0
b0 = float(input("Translation b0:")) #b0

alpha = m.radians(alpha)
print(" ")

# Affine

# Foward 
a1_f_affine = mx*(m.cos(alpha))
b1_f_affine = mx*(m.sin(alpha))
a2_f_affine = my*(m.sin(m.radians(alpha + beta)))*(-1)
b2_f_affine = my*(m.cos(m.radians(alpha + beta)))
a0_f_affine = a0
b0_f_affine = b0




print("--- Affine Foward Result ----")
print("a1     //    a2    //  a0")
print(round(a1_f_affine, 5) ,"    ",round(a2_f_affine, 5),"   ",round(a0_f_affine, 5))
print("-----------------------------")
print("b1    //    b2    //  b0")       
print(round(b1_f_affine, 5) ,"    ",round(b2_f_affine, 5),"   ",round(b0_f_affine, 5))

# Backward
a1_b_affine = -b2_f_affine/(a2_f_affine * b1_f_affine - a1_f_affine * b2_f_affine)
b1_b_affine = b1_f_affine/(a2_f_affine*b1_f_affine-a1_f_affine*b2_f_affine)
a2_b_affine = a2_f_affine/(a2_f_affine*b1_f_affine-a1_f_affine*b2_f_affine)
b2_b_affine = -a1_f_affine/(a2_f_affine * b1_f_affine - a1_f_affine * b2_f_affine)
a0_b_affine = (a0_f_affine * b2_f_affine - a2_f_affine * b0_f_affine )/(a2_f_affine * b1_f_affine - a1_f_affine * b2_f_affine)
b0_b_affine = (a1_f_affine * b0_f_affine - a0_f_affine * b1_f_affine)/(a2_f_affine * b1_f_affine - a1_f_affine * b2_f_affine)


print("--- Affine Backward Result ----")
print("a1_b     //    a2_b    //  a0_b")
print(round(a1_b_affine, 5) ,"    ",round(a2_b_affine, 5),"   ",round(a0_b_affine, 5))
print("-------------------------------")
print("b1_b    //    b2_b    //  b0_b")       
print(round(b1_b_affine, 5) ,"    ",round(b2_b_affine, 5),"   ",round(b0_b_affine, 5))

# Similarity









































