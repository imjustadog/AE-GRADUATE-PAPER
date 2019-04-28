import struct
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
from math import pi

import pywt
import struct

interval = 5
dt = 0.0000001 * interval
fs = 10000000 / interval
start = 250000
end = 450000

result = 0
pwd = os.getcwd()

#savepath = pwd + "//" + "wt_1.txt"
#fr = open(savepath, "w")

curvename = []


filepath = "extend"
    
with open(filepath, "rb") as fb:
    data = fb.read()

ch1ch2 = struct.unpack("<"+str(int(len(data)/2))+"H", data)
ch1ch2 = np.array(ch1ch2)
ch1ch2 = (ch1ch2-8192)*2.5/8192

datay1 = ch1ch2[::2]
datay2 = ch1ch2[1::2]
datax = np.array(range(len(datay1)))* 0.0000001
        
data1 = datay1[start:end:interval]
data2 = datay2[start:end:interval]
datax = datax[start:end:interval]

wavelet = 'haar'
c = pywt.central_frequency(wavelet)
fa = np.arange(400000, 20000 - 1, -200)
scales = np.array(float(c)) * fs / np.array(fa)

[cfs1,frequencies1] = pywt.cwt(data1,scales,wavelet,dt)
[cfs2,frequencies2] = pywt.cwt(data2,scales,wavelet,dt)
power1 = (abs(cfs1))
power2 = (abs(cfs2)) 

length_now = len(power1[0])
fig_size = 4000
power1 = np.reshape(power1,(len(power1),fig_size,int(length_now/fig_size)))
power2 = np.reshape(power2,(len(power2),fig_size,int(length_now/fig_size)))

power1 = np.mean(power1,axis=2)
power2 = np.mean(power2,axis=2)

corr = 0
for i in range(len(power1) - 1):
    corr += sum((power1[i] - power1[i + 1])**2)

print(corr)
