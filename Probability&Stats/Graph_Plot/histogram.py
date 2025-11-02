# Histogram
import matplotlib.pyplot as plt
import numpy as np
mu=0
sigma=1
size=1000
 
rng=np.random.default_rng()
 
data=rng.normal(mu,sigma,size)
 
plt.hist(data,bins=30,color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
 