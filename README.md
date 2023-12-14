# Baby sum-check

Educational implementation in Python of the Sum-Check protocol, based on the example provided by [Thaler](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html).

## How to run

Install required packages
```
cd <path-to-this-repo>
pip install -r requirements.txt
```

Run protocol
```
python sum-check_sympy.py
```
After running the script, following messages are printed to the console:

<pre>
start sum check
polynomial Poly(2*x1**3 + x1*x3 + x2*x3, x1, x2, x3, domain='ZZ')
Total sum over all (0,1)^v points: 12
s Poly(8*x1**3 + 2*x1 + 1, x1, domain='ZZ')
random_values {x1: 2}
s Poly(x2 + 34, x2, domain='ZZ')
random_values {x1: 2, x2: 3}
s Poly(5*x3 + 16, x3, domain='ZZ')
random_values {x1: 2, x2: 3, x3: 6}
lhs 46 oracle result 46
sum-check finished!!!

</pre>

