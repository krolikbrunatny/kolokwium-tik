import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

data = np.loadtxt("data5.txt")
x = data[:, 0] 
y = data[:, 1] 
y_err = data[:, 2]

def f(x, a, b, c, d):
    return a*x + b*x**3 + c*np.e**(d*x)

p0 = (0,0,0,0)

p, pcov = scipy.optimize.curve_fit(f, x, y, p0, sigma = y_err)

a, b, c, d = p
sigma_a, sigma_b, sigma_c, sigma_d = np.sqrt(np.diag(pcov))

#print("Dopasowanie krzywej y")
#print(f"   Parametry: {p}")

fig, ax = plt.subplots()

ax.set_xlim(-12, 12)
ax.set_ylim(-8, 18)

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title(fr"Jan Muskat $a={a:.1f} \pm {sigma_a:.1f}$, $b={b:.1f} \pm {sigma_b:.1f}$, $c={c:.1f} \pm {sigma_c:.1f}$, $d={d:.1f} \pm {sigma_c:.1f}$")

ax.errorbar(x, y, yerr = y_err, fmt = ".k", label = "Dane doświadczalne")

ax.plot(x, f(x, *p), color = "blue", label = r"Dopasowana krzywa $y=ax+bx^3+ce^(dx)$")

ax.legend()
plt.show()