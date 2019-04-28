import struct
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rc('font',family='Times New Roman',size=10)

filepath = "break/0/1"

with open(filepath, "rb") as fb:
    data = fb.read()

ch1ch2 = struct.unpack("<"+str(int(len(data)/2))+"H", data)
ch1ch2 = np.array(ch1ch2)
ch1ch2 = (ch1ch2-8192)*2.5/8192

datay1 = np.array(ch1ch2[::2]) + 0.01
datay2 = np.array(ch1ch2[1::2]) + 0.01
datax = np.array(range(len(datay1))) * 0.0000001

fig = plt.figure(figsize=(5,3))

#plt.plot(datax,datay2,color='g',label = 'ch2')
plt.plot(datax,datay1,color='b',label = 'ch1')
plt.xlabel('time/s')
plt.ylabel('amplitude/V')
plt.xlim(0,0.078)
plt.ylim(-1.5,1.5)

#ax = plt.gca()
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width, box.height])
#plt.legend(loc='upper left',bbox_to_anchor=(1,1),markerscale=2)
#plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.8)

plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)

plt.show()
