import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return np.sin(3*x)/3

def f2(x):
    return np.sin(5*x)/5

def f3(x):
    return np.sin(9*x)/9

x = np.linspace(-1.3, 1.3 , 200)


fig, ax = plt.subplots()

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-0.4, 0.4)

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Jan Muskat")

ax.plot(x, f1(x), "-", color = "yellow", label = r"$\frac{1}{3}sin3x$")
ax.plot(x, f2(x), "--", color = "red", label = r"$\frac{1}{5}sin5x$")
ax.plot(x, f3(x), ":", color = "blue", label = r"$\frac{1}{9}sin9x$")

ax.legend()

plt.show()
fig.savefig("plots.pdf")