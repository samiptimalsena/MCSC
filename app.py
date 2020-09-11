from MCSC.BisectionMethod import BisectionMethod
from MCSC.FalsePostionMethod import FalsePostionMethod
from MCSC.SecantMethod import SecantMethod
from MCSC.NewtonRaphsonMethod import NewtonRaphsonMethod
from MCSC.NewtonRaphsonMethod import GeneralizedNewtonRaphsonMethod,NewtonMethodForSystem
from MCSC.IterationMethod import IterationMethod,JacobiMethod,GaussSeidelMethod
from MCSC.ThomasAlgorithm import ThomasAlgorithm
import math

a=[-1,-1,-1]
b=[2,2,2,2]
c=[-1,-1,-1]
d=[0,0,0,1]
check=ThomasAlgorithm(a,b,c,d)
alpha,beta,X=check.calc()
print(alpha,beta,X)