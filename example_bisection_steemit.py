#Bisection Algorithm (from Steemit)
#https://steemit.com/mathematics/@dkmathstats/the-bisection-method-with-python-code

'''
    Pseudocode For Bisection Method

    if f(a)*f(b) > 0
        print("No root found")
        #Both f(a) and f(b) are the same sign
    else
        while(b - a)/2 > tolerance
            c = (b+a)/2 #c is like a midpoint
            if f(c) == 0
                return(midpoint) #The midpoint is the root such that f(midpoint) = 0
            else if f(a)*f(c) < 0
                b = c #Shrink interval from right
            else
                a = c
        return(c)
'''

# Bisection Method In Python

# Goal: Finding Roots to Polynomials
# Inputs: Function, a and b for interval [a, b], a guess in [a, b]
# Output: Roots/Zeroes To Polynomials

# Reference: Tim Sauer - Numerical Analysis Second Edition
# http://code.activestate.com/recipes/578417-bisection-method-in-python/

# https://stackoverflow.com/questions/6289646/python-function-as-a-function-argument

def f(x):
    return (x**2 - 11)

def bisection_method(a, b, tol):
    if f(a)*f(b) > 0:
        #end function, no root
        print("No root found.")
    else:
        while(b-a)/2.0 > tol:
            midpoint = (a+b)/2.0
            if f(midpoint) == 0:
                return(midpoint) #The midpoint is the x-intercept/root.
            elif f(a)*f(midpoint) < 0: #Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint
        return(midpoint)

answer = bisection_method(-1, 5, 0.0001)
print("Answer: ", round(answer, 3))
#Answer: 3.317
