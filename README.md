# MCSC

MCSC is a package for solving numerical methods problems. Currently only root-finding algorithms are available such as:-

  - Bisection Method
  - Fase Position Method
  - Secant Method
  - Iteration Method -> Gauss Seidel and Jacobi Method
  - Newton Raphson Mehod -> Generalized as well as for system of non linear equations.
  - Thomas Algorithm

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

For Iteration method and other methods for solving system of equations you need to pass initial approximation and required functions in form of list:

```sh
from MCSC.IterationMethod import JacobiMethod

def fun_1(x,y,z):
    return x**2+y**2+z**2+10*x-4
def fun_2(x,y,z):
    return x**2-y**2+z**2+10*y-5
def fun_3(x,y,z):
    return  x**2+y**2-z**2+10*z-6

def fun_x(x,y,z):
    return (4-x**2-y**2-z**2)/10
def fun_y(x,y,z):
    return (5-x**2+y**2-z**2)/10
def fun_z(x,y,z):
    return (6-x**2-y**2+z**2)/10

method=JacobiMethod([0,0,0],[fun_1,fun_2,fun_3,fun_x,fun_y,fun_z])
print(method.calc())
```

Run the sample.py file in similar way as above.


License
----

MIT

Want to contribute? Great!

**Free Software, Hell Yeah!**


