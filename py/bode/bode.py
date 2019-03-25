import numpy as np
import matplotlib.pyplot as plt
import math

plt.rc('font',family='Times New Roman',size=10)

w = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,400000,500000,1000000,2000000,3000000,4000000,5000000,8000000,9000000,10000000,20000000]

p = [0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.086,0.704,4.6,5.4,5.08,5.04,4.08,2.96,0.3,0.14,0.1,0.08,0.06,0.07,0.07,0.08,0.08]
p = [20.0 * math.log(x / 5.0) for x in p]

fig = plt.figure(figsize=(5,3))
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.75)
plt.semilogx(w, p, linewidth=2)
plt.xlabel('frequency/Hz')
plt.ylabel('gain/dB')

plt.savefig('bode.pdf')
plt.show()
