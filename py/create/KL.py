from math import pi, log
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman',size=10) 

result = []
p=0.2
ha = [i * 0.001 for i in range(1,1000)]

for pj in ha:
    result.append(p * log(p/pj)+ (1-p)*log((1-p)/(1-pj)))

plt.rc('font',family='Times New Roman',size=10)
fig = plt.figure(figsize=(4,3))
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)
plt.plot(ha,result)
plt.xlabel('KL divergence')
plt.ylabel(r'$\hat h_j$')
plt.show()
