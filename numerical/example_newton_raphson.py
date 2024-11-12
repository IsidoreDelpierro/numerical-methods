#Newton-Raphson Method
import math

def derivative(f, x, dx = 1e-6):
	df = f(x + dx) - f(x - dx)
	return df/(2*dx)

def newton(f, x0, tol = 1e-10, maxit = 100):
	x = x0
	fx = f(x)


	for _ in range(maxit):

		if abs(fx) < tol:
			break

		fpx = derivative(f, x)
		if abs(fpx) < tol:
			break

		x = x - fx/fpx
		fx = f(x)

	return x

func = lambda x: x**2 - x - 1
x0 = 2
x = newton(func, x0, tol = 1e-10, maxit = 100)
print("Solution: x = {}, f(x) = {}".format(x, func(x)))

func2 = lambda x: x**2 - math.exp(-x) - 1
x0 = 2
x = newton(func2, x0, tol = 1e-10, maxit = 100)
print("Solution: x = {}, f(x) = {}".format(x, func2(x)))
