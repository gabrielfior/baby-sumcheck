import itertools

class Prover:
    def __init__(self, poly, vars) -> None:
        self.poly = poly
        self.vars = vars
    
    def calculate_sum(self, num_vars_to_iterate, subs = {}):
        total_sum = 0
        coords = list(itertools.product("01", repeat=num_vars_to_iterate))
        poly = self.poly
        # apply substitutions for random values
        for k,v in subs.items():
            poly = poly.subs(k,v)
        for coord_items in coords:
            curr_poly = poly
            for idx,value in enumerate(coord_items):
                curr_poly =  curr_poly.subs(self.vars[idx],value)
                #print (f'curr_poly {curr_poly}')
            total_sum += curr_poly
        return total_sum    
    
