import math
import numpy as np
import matplotlib.pyplot as plt

# Probability distribution function 
#X axis is values of random variables 
#Y axis will contain probability of that points according to random variables
# distance between P and Q is d.
plt.xlabel('k')
plt.ylabel('Pr(A<=k)')
Amount = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]
Prob = [0,0.0625,0.0625,0.0625,0.3125,0.3125,0.6875,0.6875,0.6875,0.9375,0.9375,1,1]
plt.xlim([-8,6])
plt.ylim([-0.5,1.5])
plt.scatter(Amount,Prob,marker='o')


plt.show()
