class Verifier:
    def __init__(self) -> None:
        pass

    def get_variable_from_univ_poly(self, poly):
        if len(list(poly.free_symbols)) > 1:
            raise Exception("Polynomials must be univariate")
        symbol = list(poly.free_symbols)[0]
        return symbol

    def verify_univariate_poly(self, poly_s, poly_prev, random_value = 0):
                
        symbol = self.get_variable_from_univ_poly(poly_s)
        # We sum poly_s at points 0 and 1
        lhs = poly_s.subs(symbol, 0) + poly_s.subs(symbol, 1)
        # ToDo - Pass polynomials as list of coefficients
        # instead of passing objects around
        if len(poly_prev.free_symbols) == 0:
            # nothing to subst
            rhs = poly_prev
        else:
            symbol = self.get_variable_from_univ_poly(poly_prev)
            rhs = poly_prev.subs(symbol, random_value)
        
        if lhs != rhs:
            raise Exception('poly_s and poly_prev dont match')

    def assert_poly_matches_external_query(self, poly, random_value, oracle_result):
        symbol = self.get_variable_from_univ_poly(poly)
        lhs = poly.subs(symbol, random_value)
        print (f'lhs {lhs} oracle result {oracle_result}')
        if lhs != oracle_result:
            raise Exception("lhs and oracle_result dont match")
