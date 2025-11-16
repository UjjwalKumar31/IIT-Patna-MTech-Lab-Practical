import matplotlib.pyplot as plt
 
Sub=['Hindi','Maths','Eng','Phy','Che']
Marks=[80,90,75,65,70]
plt.pie(Marks,labels=Sub, autopct='%0.2f%%',
        colors=['lightblue','lightcoral','yellow', 'lightgreen','red'],startangle=90)
plt.show()