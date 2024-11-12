#Gauss-Seidal Method
from numpy import*

a = int(input("\nEnter the first limit: \n"))
b = int(input("\nEnter the second limit: \n"))
xm = (a+b)/2
def f(x):
	y=x*x-4
	return y

if f(a)*f(b) < 0:
	while abs(f(xm)>0.0001):
		if f(a)*f(xm) > 0:
			a = xm
		else:
			b = xm
		xm = (a+b)/2
	print("\nThe root is ", xm)

else:
	print("\nThe limits are not valid")
