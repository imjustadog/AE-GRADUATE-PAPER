import struct
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rc('font',family='Times New Roman',size=10)

pwd = os.getcwd()
fb = open(pwd + "\\"+ "new\\40" + "\\" + "2", "rb")

x = 0
datax = []
datay1 = []
datay2 = []
index1 = 0
index2 = 0
while True:
    data = fb.read(4)
    if not data:
        break
    ch1, ch2 = struct.unpack('<HH', data)
    ch1 = (float(ch1) - 8192) / 8192 * 2.5
    ch2 = (float(ch2) - 8192) / 8192 * 2.5
    ch1 = float(ch1)
    ch2 = float(ch2)
    x = x + 1
    datax.append(x * 0.0000001)
    datay1.append(ch1)
    datay2.append(ch2)
    if x >= 10:
        if ch1 > 0.3 :
            index1 = x - 1
        if ch2 > 0.3 :
            index2 = x - 1
print (index2 - index1)* 0.0000001

fig = plt.figure(figsize=(5,3))
plt.plot(datax,datay2,color='b')
plt.plot(datax,datay1,color='g')
plt.xlabel('time/s')
plt.ylabel('amplitude/V')
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)
plt.show()
