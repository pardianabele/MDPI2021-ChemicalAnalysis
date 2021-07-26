import matplotlib.pyplot as plt
import numpy as np

fig, (f1a, f1b, f1c) = plt.subplots(1, 3, figsize=(20, 5))

#------------------------------------ product types - Figure 1a ----------------------------

x = np.arange(0, 6000, 1)
k = 0.001
X0 = 1
Y0 = 1.5
x_1 = X0 * np.exp(-k*x)
x_3 = Y0 * np.exp(-k*x)

f1a.plot(x, x_3, '#03f962', label=r'$X(t)$', linewidth=7)
f1a.plot(x, x_1, '#f22114', label=r'$Y(t)$', linewidth=7)
f1a.xaxis.set_tick_params(labelsize=15)
f1a.yaxis.set_tick_params(labelsize=15)
f1a.set_xlabel('t (s)', fontsize=20)
f1a.set_ylabel(r'concentration ($10^{-20}$ M)', fontsize=20)
f1a.legend(fontsize=20)

#------------------------------------ conventional currency - Figure 1b ------------------------

x = np.arange(0, 6000, 1)
k1 = 0.001
a = 4
x_1 = a * np.exp(-k1*x)

f1b.plot(x, x_1, '#7c1186', label=r'$A(t)$', linewidth=7)
f1b.set_xlabel('t (s)', fontsize=20)
f1b.xaxis.set_tick_params(labelsize=15)
f1b.yaxis.set_tick_params(labelsize=15)
f1b.legend(fontsize=20)

#------------------------------------ currency types - Figure 1c  ----------------------------

x = np.arange(0, 6000, 1)
k1 = 0.001
a = 2
c = 1.5
x_1 = a * np.exp(-k1*x)
x_2 = c * np.exp(-k1*x)

f1c.plot(x, x_1, '#7c1186', label=r'$A(t)$', linewidth=7)
f1c.plot(x, x_2, '#FFA500', label=r'$C(t)$', linewidth=7)
f1c.set_xlabel('t (s)', fontsize=20)
f1c.xaxis.set_tick_params(labelsize=15)
f1c.yaxis.set_tick_params(labelsize=15)
f1c.legend(fontsize=20)

plt.tight_layout()
fig.savefig("Figure1.png")
