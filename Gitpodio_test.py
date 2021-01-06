import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#print(random.normal(size=100))

x = np.linspace(0,7,100)
y =np.sin(x)

plt.plot(x,y)
plt.grid()
plt.show()
plt.savefig("test.png")