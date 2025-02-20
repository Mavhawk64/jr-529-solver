import sympy as sp

# R = 0.05 # Annual interest rate
# r = R/12 # Monthly interest rate
# P = 1000 # Monthly payment
# n = 18 * 12 # Number of payments

fv, p, r, n = sp.symbols('FV P r n', real=True, positive=True)

eq = sp.Eq(fv, p*((1+r)**n-1)/r)

# solve for p
p = sp.solve(eq, p)

# print(sp.latex(p[0]))

fv = 1e5
r = 0.05 / 12
n = 18 * 12

pmt = fv * r / ((r + 1)**n - 1)

print(pmt * 3)
