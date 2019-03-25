import struct
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font',family='Times New Roman',size=10)

fb = open("1M", "rb")
x = 0
datax = []
datay1 = []
datay2 = []
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
    if(x > 100):
        break
    datax.append(x * 0.0001)
    datay1.append(ch1)
    datay2.append(ch2)

nfft = 64
# plot x-t, time-domain, i.e. source waveform
#plt.subplot(211)
fig = plt.figure(figsize=(5,3))
plt.plot(datax,datay1,color='b')
#plt.plot(datax,datay2,color='g')
plt.xlabel('time/ms')
plt.ylabel('amplitude/V')
plt.ylim(-0.4,0.4)
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)

# plot power(f)-t, frequency-domain, i.e. spectrogram
# call specgram function, setting Fs (sampling frequency) 
# and nfft (number of waveform samples, defining a time window, 
# for which to compute the spectra)

#fig = plt.subplot(212)
#cmap = plt.get_cmap('gist_rainbow') # this may fail on older versions of matplotlib
#cmap.set_under(color='k', alpha=None)
#pxx, freq, t, cax = plt.specgram(datay, cmap=cmap, Fs=10000000, NFFT=nfft, noverlap=nfft/4, detrend='mean', mode='psd')
#cbar = plt.colorbar(cax)
#plt.xlabel('time')
#plt.ylabel('frequency/Hz')


#xf = np.fft.fft(datay)
#N = len(xf)
#xf = np.abs(xf) / (N / 2)

#xf_abs = xf[0:int(N/2)]
#xf_abs[0] = xf_abs[0] / 2
#axis_xf = range(int(N/2))
#freq = [x * 10000000.0 / N for x in axis_xf]
#plt.subplot(212)
#plt.plot(freq,xf_abs)    
#plt.xlabel('kHz')

#plt.savefig('24.pdf')
plt.show()
