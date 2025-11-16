import numpy as np
# Function to compute g(k) (from Eq. 6)
def g_k(k, data):
    n = len(data)
    sum_x_k = np.sum(data ** k)
    sum_x_k_log_x = np.sum((data ** k) * np.log(data))
    sum_log_x = np.sum(np.log(data))
 
    # g(k) as per Eq. 6
    g_k_value = (n / k) - n * (sum_x_k_log_x / sum_x_k) + sum_log_x
    return g_k_value
 
# Function to compute g'(k) (from Eq. 7)
def g_prime_k(k, data):
    n = len(data)
    sum_x_k = np.sum(data ** k)
    sum_x_k_log_x = np.sum((data ** k) * np.log(data))
    sum_x_k_log_x_squared = np.sum((data ** k) * (np.log(data) ** 2))
 
    # g'(k) as per Eq. 7
    term1 = -n / k**2
    term2 = n * (sum_x_k_log_x_squared * sum_x_k - sum_x_k_log_x**2) / (sum_x_k**2)
 
    g_prime_k_value = term1 - term2
    return g_prime_k_value
 
##  Newton-Raphson Method
def newton_raphson(data,init_k,tol=1e-5, max_iter=100):
  k=init_k
  for i in range(max_iter):
    g_k_new=g_k(k, data)
    g_k_prime=g_prime_k(k, data)
    k_new=k-g_k_new/g_k_prime
    if abs(k_new-k)<tol:
      return k_new
    k=k_new
  raise ValueError("NR did not converge for this initial guess")
 
## estimate  lambada (Eq (3))
def estimate_lambada(k,data):
  n=len(data)
  lambada=(np.sum(data**k)/n)**(1/k) # From equation number (3)
  return lambada
 
rng=np.random.default_rng(42)
lam=2
data=rng.weibull(a=1.5,size=100)*lam
 
init_k=1.5
k_estimate=newton_raphson(data,init_k,tol=1e-5, max_iter=100)
lambada_estimate=estimate_lambada(k_estimate,data)
print(f"Genrated samples are {data}")
print(f"Estimated value of k is {k_estimate}")
print(f"Estimated value of lambda is {lambada_estimate}")