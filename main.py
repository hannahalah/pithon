import numpy as np

x=1.5
a1=np.sin(np.pi/2+1)**2
a2=x*(3+x**2)**0.25
a3=np.tan(x**3-1)**3
z=np.arctan(x/2)-np.log(17.56)
y=(a1+a2-a3)/z
print(y)