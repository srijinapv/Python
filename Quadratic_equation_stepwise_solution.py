from sympy import *
import numpy as np
import math

a = int(input("coeficient of X^2 :"))
b = int(input("coeficient of X:"))
c = int(input("enter the constant:"))

def valueX(a ,b,c):
    D = b*b - 4*a*c
    X1 = (-b + sqrt(D))/(2*a)
    X2 = (-b - sqrt(D))/(2*a)
    X1 = (-b + sqrt(D))/(2*a)

    print("\n")

    print("X = (-b + sqrt(D))/(2*a) and X = (-b + sqrt(D))/(2*a) ")

    print("\n")

    print("Substitute values of b , D and a in the above formula ")

    print("\n")

    print(f'Values of X = {X1} , {X2}')

    print("\n")

    return X1,X2

D = b*b - 4*a*c
print("D = b*b - 4*a*c ")
print("\n")
print(f'By applying values of a,b,c we get D = {D}')
print("\n")
if D > 0:
    print("D is greater than 0 there fore roots are real and distinct.")
    valueX(a ,b,c)

elif D < 0 :
    print("D is less than 0 there fore roots do not exist, or the roots are imaginary.")
    valueX(a ,b,c)

else :

    print("D = 0, the roots are real and equal.")
    valueX(a ,b,c)