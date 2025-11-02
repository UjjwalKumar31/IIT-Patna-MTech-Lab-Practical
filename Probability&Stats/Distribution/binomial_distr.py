# Binomial distribution without using scipy
from math import comb
import numpy as np
 
def binomial_exp(n,p):
   x=np.arange(0,n+1)
   pmf=[comb(n,k)*(p**k)*((1-p)**(n-k)) for k in x]
 
   exp_x=np.sum([k*pmf[k] for k in x])
   exp_xx=np.sum([(k**2)*pmf[k] for k in x])
   var_b=exp_xx-(exp_x)**2
 
   return exp_x,var_b
 
n=10
p=0.5
mean_b,var_b=binomial_exp(n,p)
 
print(f"Mean of the binomial distribution is {mean_b}")
print(f"Variance of the binomial distribution is {var_b}")

# Binomial distribution  using scipy
from scipy.stats import binom
 
n=10
p=0.5
mean_bn=binom.mean(n,p)
var_bn=binom.var(n,p)
 
print(f"Mean of the binomial distribution is {mean_bn}")
print(f"Variance of the binomial distribution is {var_bn}")

# Write a code to find out mean and variance of the Poisson and Geometric distribution
# Method I
import numpy as np
from scipy.stats import poisson, geom
 
def poisson_stats(lmbda):
    mean = poisson.mean(mu=lmbda)
    var = poisson.var(mu=lmbda)
    return mean, var
 
def geometric_stats(p):
    mean = geom.mean(p)
    var = geom.var(p)
    return mean, var
 
# Example values
lmbda = 5    # Poisson parameter (mean rate)
p = 0.25     # Geometric success probability
 
poisson_mean, poisson_var = poisson_stats(lmbda)
geometric_mean, geometric_var = geometric_stats(p)
 
print("Poisson mean:", poisson_mean)
print("Poisson variance:", poisson_var)
print("Geometric mean:", geometric_mean)
print("Geometric variance:", geometric_var)

# Method II
import numpy as np
from scipy.stats import poisson, geom
lmbda = 5     
p = 0.25      

poisson_mean = poisson(lmbda).mean()
poisson_var = poisson(lmbda).var()

geometric_mean = geom(p).mean()
geometric_var = geom(p).var()

print("Poisson mean:", poisson_mean)
print("Poisson variance:", poisson_var)
print("Geometric mean:", geometric_mean)
print("Geometric variance:", geometric_var)

#Skreness and Kurtosis
from math import comb
import numpy as np
 
def binomial_gamma(n,p):
   x=np.arange(0,n+1)
   pmf=[comb(n,k)*(p**k)*((1-p)**(n-k)) for k in x]
 
   exp_x=np.sum([k*pmf[k] for k in x])
   mu_2=np.sum([((k-exp_x)**2)*pmf[k] for k in x])
   mu_3=np.sum([((k-exp_x)**3)*pmf[k] for k in x])
   mu_4=np.sum([((k-exp_x)**4)*pmf[k] for k in x])
   gamma_1=mu_3/(mu_2**(3/2))
   gamma_2=mu_4/(mu_2*2)
   return gamma_1,gamma_2

n=10
p=0.5
gamma1,gamma2=binomial_gamma(n,p)
print(f"The skewness coefficient is {gamma1}") #0.0 : Symmetric
print(f"The kurtosis coefficient is {gamma2}") #3.5 : Leftokurtic