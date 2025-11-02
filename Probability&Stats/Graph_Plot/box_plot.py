# Box Plot
import matplotlib.pyplot as plt
import numpy as np
 
mu=0
sigma=1
size=100
 
rng=np.random.default_rng()
data=rng.normal(mu,sigma,size)
data=np.append(data,[7,-6,5,-3])
plt.figure(figsize=(4,2))
plt.boxplot(data,vert=False,patch_artist=True)
plt.show()