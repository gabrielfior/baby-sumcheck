import sys
from sympy import *
from sympy.core.random import _randint
from prover import Prover
from oracle import Oracle
from verifier import Verifier

# Initialization
print ('start sum check')
x1, x2, x3 = symbols("x1 x2 x3")
poly = Poly(2*x1**3 + x1*x3 + x2*x3)
idx_to_vars = {0: x3, 1: x2, 2: x1}
p = Prover(poly, idx_to_vars)
v = Verifier()
print (f'polynomial {poly}')
num_of_rounds = len(poly.free_symbols)

# ToDo - Divide in prover, verifier, etc
### Round 1
# Prover (P) sends value of sum to verifier (V)
total_sum = p.calculate_sum(3)
print (f'Total sum over all (0,1)^v points: {total_sum}')

random_values = {}
vars_to_iterate = num_of_rounds-1
prev_s = total_sum
random_values_store = [2,3,6]
random_value = 0
for round_idx in range(3):
    s = p.calculate_sum(vars_to_iterate, random_values)
    print (f's {s}')

    # Verifier checks that s1(0) + s1(1) = 12
    v.verify_univariate_poly(s, prev_s, random_value)

    random_value = random_values_store.pop(0)
    # We fetch the random_value idx in desc order
    x_variable = idx_to_vars[num_of_rounds-round_idx-1]
    random_values[x_variable] = random_value
    print (f'random_values {random_values}')

    prev_s = s
    vars_to_iterate -= 1

# Final round, verifies executes oracle query

#result_from_oracle = poly.subs(x1,r1).subs(x2,r2).subs(x3,r3)
result_from_oracle = Oracle().evaluate_polynomial(poly, 
                                                  random_values)

# Verifier checks that s3(6) = g(r1,r2,r3)
v.assert_poly_matches_external_query(s, random_value, result_from_oracle)

print ('sum-check finished!!!')