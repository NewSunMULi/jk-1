import matplotlib.pyplot as plt
import math
import numpy as np

cOH = 0.1
vo = 0.02
cH2SO4 = 0.1
vh = np.linspace(0, 0.02, 100).tolist()
vb = [0.001, 0.002, 0.004, 0.005, 0.008, 0.01, 0.012, 0.014, 0.015, 0.017, 0.02]
vm = []
vx = []
for i in vh:
    if i < 0.01:
        vm.append(math.log((10 ** -14)/((0.1*0.02-0.2*i)/(0.02 + i)), 10)*-1)
    else:
        vm.append(math.log(-(0.1 * 0.02 - 0.2 * i) / (0.02 + i), 10) * -1)

for i in vb:
    if i < 0.01:
        print(math.log((10 ** -14) / ((0.1 * 0.02 - 0.2 * i) / (0.02 + i)), 10) * -1)
        vx.append(math.log((10 ** -14) / ((0.1 * 0.02 - 0.2 * i) / (0.02 + i)), 10) * -1)
    elif i == 0.01:
        vx.append(7)
    else:
        print(math.log((0.2 * i - 0.002) / (0.02 + i), 10) * -1)
        vx.append(math.log((0.2 * i - 0.002) / (0.02 + i), 10) * -1)
plt.plot(vh, vm)
plt.scatter(vb, vx)
plt.show()