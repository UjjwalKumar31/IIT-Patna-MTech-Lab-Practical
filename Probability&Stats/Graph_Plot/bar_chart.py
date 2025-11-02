# Bar chart
import matplotlib.pyplot as plt
import numpy as np
 
subject=['Hindi','Eng','Maths','Science','Social Science']
A=[75, 90, 70,60,90]
B=[80,50,95,89,70]
n=len(subject)
x=np.arange(n)
width=0.35 # Width of the bar
 
plt.bar(x-width/2,A,width)
plt.bar(x+width/2,B,width)
plt.xticks(x,subject)
plt.title('Bar chart')
plt.xlabel('subject')
plt.ylabel('marks')
plt.legend(['StudentA', 'StudentB'])