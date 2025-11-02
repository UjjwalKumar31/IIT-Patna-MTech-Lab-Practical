# Line Plot
import matplotlib.pyplot as plt
import numpy as np
 
x=np.linspace(-2*np.pi,2*np.pi,100)
y=np.sin(x)
plt.plot(x,y,color='green')
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()