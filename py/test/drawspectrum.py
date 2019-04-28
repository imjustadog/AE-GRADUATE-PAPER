import struct
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal

#total data:786432 ch1 ch2

plt.rc('font',family='Times New Roman',size=10)

filepath = "3100/1"

with open(filepath, "rb") as fb:
    data = fb.read()

ch1ch2 = struct.unpack("<"+str(int(len(data)/2))+"H", data)
ch1ch2 = np.array(ch1ch2)
ch1ch2 = (ch1ch2-8192)*2.5/8192

datay1 = ch1ch2[::2]
datay2 = ch1ch2[1::2]
datax = np.array(range(len(datay1)))* 0.0000001
        
datay1 = datay1[200000:700000]
datay2 = datay2[200000:700000]
count = len(datay1)

fftnum = 10000
std = 1500
fftrepeat = 0

axis_xf = range(int(fftnum/2))
freq = [i * 10000000.0 / fftnum for i in axis_xf]

index = 0
magnitude1 = []
magnitude2 = []
while True:
    data1 = np.array(datay1[index:index + fftnum])
    data2 = np.array(datay2[index:index + fftnum])
    win = signal.gaussian(fftnum, std)
    data1 = np.multiply(data1,win)
    data2 = np.multiply(data2,win)
    data1 = np.abs(np.fft.fft(data1, fftnum)) / (fftnum / 2)
    data2 = np.abs(np.fft.fft(data2, fftnum)) / (fftnum / 2)
    magnitude1.append(data1)
    magnitude2.append(data2)
    index += int(fftnum * (1 - fftrepeat))
    if index + fftnum > count:
        break

mag1 = sum(np.array(magnitude1)) / len(magnitude1)
mag2 = sum(np.array(magnitude2)) / len(magnitude2)

start = int(10000 / (10000000.0 / fftnum))
end = int(400000 / (10000000.0 / fftnum))

freq = np.array(freq[start:end])
mag1 = mag1[start:end]
mag2 = mag2[start:end]

freq = freq/1000

fig = plt.figure(figsize=(5,3))
plt.plot(freq,mag1,color='b',label='ch1')
plt.plot(freq,mag2,color='g',label='ch2')
plt.xlim(freq[0],freq[-1])
plt.xlabel('kHz')
plt.ylabel('amplitude/V')

ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height])
plt.legend(loc='upper left',bbox_to_anchor=(1,1),markerscale=2)
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.8)

#plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)

plt.show()
