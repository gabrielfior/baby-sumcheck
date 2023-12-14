class Oracle:

    def evaluate_polynomial(self, poly, subs):
        for k,v in subs.items():
            poly = poly.subs(k,v)
        return poly