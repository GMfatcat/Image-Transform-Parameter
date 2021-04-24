# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:56:11 2021

@author: user
"""


import math

print("Start....")


alpha = float(input("Rotation Angle Alpha:")) 
m = float(input("Scaling:")) 
a0 = float(input("Translation a0:")) #a0
b0 = float(input("Translation b0:")) #b0
print(" ")

# similarity

# Foward 
a1_f_similarity = m*(math.cos(math.radians(alpha)))
b1_f_similarity = m*(math.sin(math.radians(alpha)))
a0_f_similarity = a0
b0_f_similarity = b0

print("--- similarity Foward Result ----")
print("a1     //    a0")
print(round(a1_f_similarity, 5) ,"    ",round(a0_f_similarity, 5))
print("-----------------------------------")
print("b1     //     b0")       
print(round(b1_f_similarity, 5) ,"    ",round(b0_f_similarity, 5))

# Backward
a1_b_similarity = a1_f_similarity/(pow(a1_f_similarity,2) + pow(b1_f_similarity,2))
b1_b_similarity = -b1_f_similarity/(pow(a1_f_similarity,2) + pow(b1_f_similarity,2))
a0_b_similarity = -(a1_f_similarity * a0_f_similarity + b1_f_similarity * b0_f_similarity )/(pow(a1_f_similarity,2) + pow(b1_f_similarity,2))
b0_b_similarity = (a0_f_similarity * b1_f_similarity - a1_f_similarity * b0_f_similarity )/(pow(a1_f_similarity,2) + pow(b1_f_similarity,2))


print("--- similarity Backward Result ----")
print("a1_b     //     a0_b")
print(round(a1_b_similarity, 5) ,"    ",round(a0_b_similarity, 5))
print("-----------------------------------")
print("b1_b    //      b0_b")       
print(round(b1_b_similarity, 5) ,"    ",round(b0_b_similarity, 5))