# MCSC

MCSC is a package for solving numerical methods problems. Currently only root-finding algorithms are available such as:-

  - Bisection Method
  - Iteration Method -> Gauss Seidel and Jacobi Method
  - Newton Raphson Mehod -> Generalized as well as for system of non linear equations.

### Installation

```sh
$ pip install MCSC
```


# Demo
Open your favourite code editor and create a sample.py file with following codes:

```sh
from MCSC.BisectionMethod import BisectionMethod
import math

a=0
b=-1
def function(x):
    return 2*x*math.cos(2*x)-(x+1)**2
method=BisectionMethod(a,b,function)
steps,table=method.calc()
print(table)
```

Run the sample.py file and you will see a beautiful table which has your precise solution.
```sh
$ python sample.py
```


License
----

MIT

Want to contribute? Great!

**Free Software, Hell Yeah!**


