import matplotlib.pyplot as plt
import numpy as np
mu=0
sigma=1
size=1000
 
rng=np.random.default_rng()
 
data1=rng.normal(mu,sigma,size)
data2=rng.normal(2,2,size)
plt.scatter(data1,data2)