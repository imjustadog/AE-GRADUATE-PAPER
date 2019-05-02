import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman',size=10)

y = []
with open("train",'r') as fr:
    for line in fr.readlines():
        line = line.strip()
        y.append(float(line))

fig = plt.figure(figsize=(4,3))
plt.xlabel("epoch")
plt.ylabel("target")
plt.ylim(0,1000)
plt.plot(y)
plt.subplots_adjust(bottom = 0.2,left = 0.15,right=0.9)
plt.show()
