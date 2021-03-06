#Newton-Raphson Method (Math Python)
#https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/


def newton(f, Df, x0, epsilon, max_iter):
	'''Approximate solution of f(x)=0 by Newton's method.

	Parameters
	----------
	f : function
		Function for which we are searching for a solution f(x)=0.
	Df : function
		Derivative of f(x)
	x0 : number
		Initial guess for a solution f(x)=0.
	epsilon : number
		Stopping criteria is abs(f(x)) < epsilon.
	max_iter : integer
		Maximum number of iterations of Newton's method.

	Returns
	-------
	xn : number
		Implement Newton's method: compute the linear approximation
		of f(x) at xn and find x intercept by the formula
			x = xn - f(xn)/Df(xn)
		Continue until abs(f(xn)) < epsilon and return xn.
		If Df(xn) == 0, return None. If the number of iterations
		exceeds max_iter, then return None.

	Examples
	--------
	>>> f = lambda x: x**2 - x - 1
	>>> Df = lambda x: 2*x - 1
	>>> newton(f,Df,1,1e-8,10)
	Found solution after 5 iterations.
	1.618033988749989
	'''

	xn = x0
	for n in range(0,max_iter):
		fxn = f(xn)
		if abs(fxn) < epsilon:
			print('\nFound solution after ',n,' iterations\n')
			return xn
		Dfxn = Df(xn)
		if Dfxn == 0:
			print('Zero derivative. No solution found.')
			return None
		xn = xn - fxn/Dfxn
	print('Exceeded maximum iterations. No solution found.')
	return None

#Convergent Example: Supergolden Ratio
p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = newton(p,Dp,1,1e-10,10)
print(approx)

#Divergent Example
f = lambda x: x**(1/3)
Df = lambda x: (1/3)*x**(-2/3)
approx = newton(f, Df, 0.1, 1e-2, 100)
