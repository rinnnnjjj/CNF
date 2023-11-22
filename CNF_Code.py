from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, to_cnf

# Define the symbols (variables) used in the expression
P, Q, R, S, T = symbols('P Q R S T')

# Input expression using sympy's logical functions
# Equivalent(P, Or(Q, R)) represents (P == (Q | R))
# Implies(S, Not(T)) represents (S >> ~T)
input_expr = And(Equivalent(P, Or(Q, R)), Implies(S, Not(T)))

# Convert the expression to Conjunctive Normal Form (CNF)
cnf_expr = to_cnf(input_expr, simplify=True)

# Print the CNF expression
print(cnf_expr)
