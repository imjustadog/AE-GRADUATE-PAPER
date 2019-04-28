import struct
import matplotlib.pyplot as plt
import numpy as np
import os
import pywt

plt.rc('font',family='Times New Roman',size=10)
cmap = plt.get_cmap('rainbow') 

interval = 5
dt = 0.0000001 * interval
fs = 10000000 / interval

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

datay1 = datay1[241693:441693]
datay1[20400:28306] = datay1[20400:28306] + 0.013
datax = np.array(range(len(datay1))) * 0.0000001 

data1 = datay1[0:200000:5]
datax = datax[0:200000:5]

wavelet = 'morl'
c = pywt.central_frequency(wavelet)
fa = np.arange(400000, 20000 - 1, -200)
scales = np.array(float(c)) * fs / np.array(fa)

[cfs1,frequencies1] = pywt.cwt(data1,scales,wavelet,dt)
power1 = (abs(cfs1))

length_now = len(power1[0])
fig_size = 4000
power1 = np.reshape(power1,(len(power1),fig_size,int(length_now/fig_size)))
power1 = np.mean(power1,axis=2)

#power1 = np.log10(power1)
#power2 = np.log10(power2)

#mx = power1.max()
#mn = power1.min()
#power1 = (power1-mn) / (mx-mn) * 255.0

#mx = power2.max()
#mn = power2.min()
#power2 = (power2-mn) / (mx-mn) * 255.0

#plt.subplot(2,1,1)
fig = plt.figure(figsize=(6,3))
gci1 = plt.imshow(power1,cmap=cmap)
cbar = plt.colorbar(gci1,extend = 'max')
plt.clim(0,0.6)
ax=plt.gca()
ax.set_yticks(np.linspace(0,1900,5))
ax.set_yticklabels(('400', '305', '210', '115', '20'))
ax.set_xticks(np.linspace(0,4000,5))
ax.set_xticklabels(('0', '0.005', '0.01','0.015','0.02'))
plt.ylabel("frequency/kHz")
plt.xlabel("time/s")

#plt.subplot(2,1,2)
#gci2 = plt.imshow(power2,cmap=cmap)
#cbar = plt.colorbar(gci2)
#ax=plt.gca()
#ax.set_yticks(np.linspace(0,1900,5))
#ax.set_yticklabels(('400', '305', '210', '115', '20'))
#ax.set_xticks(np.linspace(0,4000,6))
#ax.set_xticklabels(('0', '0.002', '0.004','0.006','0,008','0.01'))
#plt.xlabel("time/s")
#plt.ylabel("frequency/kHz")

plt.show()


