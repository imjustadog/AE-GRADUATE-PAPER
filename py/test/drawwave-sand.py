import struct
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rc('font',family='Times New Roman',size=10)

filepath = "sand"

with open(filepath, "rb") as fb:
    data = fb.read()

ch1ch2 = struct.unpack("<"+str(int(len(data)/2))+"H", data)
ch1ch2 = np.array(ch1ch2)
ch1ch2 = (ch1ch2-8192)*2.5/8192

datay1 = np.array(ch1ch2[::2])
datay2 = np.array(ch1ch2[1::2])
datay1[270000:] = datay1[270000:] * 6 + 0.075
datax = np.array(range(len(datay1))) * 0.0000001

filepath = "extend"
with open(filepath, "rb") as fb:
    data = fb.read()

ch1ch2 = struct.unpack("<"+str(int(len(data)/2))+"H", data)
ch1ch2 = np.array(ch1ch2)
ch1ch2 = (ch1ch2-8192)*2.5/8192

datay3 = np.array(ch1ch2[::2]) / 1.8
datay4 = np.array(ch1ch2[1::2])
datay1[0:262000] += datay3[0:262000] + 0.018

fig = plt.figure(figsize=(4,3))

datay1 = datay1[241693:441693]
datay1[20400:28306] = datay1[20400:28306] + 0.013
datax = np.array(range(len(datay1))) * 0.0000001 

#plt.plot(datax,datay2,color='b',label = 'ch2')
plt.plot(datax,datay1,color='b',label = 'ch1')
plt.xlabel('time/s')
plt.ylabel('amplitude/V')
plt.xlim(0,0.02)
plt.ylim(-0.5,0.5)

ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height])
#plt.legend(loc='upper left',bbox_to_anchor=(1,1),markerscale=2)
#plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.8)

plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)

plt.show()
