import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

data = np.loadtxt("data1.txt")
v = data[:, 0] # [wiersz, kolumna], tu: wszystkie wiersze i pierwsza (zerowa) kolumna.
a = data[:, 1] # [wiersz, kolumna], tu: wszystkie wiersze i druga (pierwsza) kolumna.


###############################################################################
# Dopasowanie prostej y = a x + b do danych doświadczalnych.
###############################################################################

# Funkcja zadająca krzywą y = f(x), która ma zostać dopasowana.
# Na liście argumentów muszą się też znaleźć parametry dopasowania: a i b.
g = 9.8
m = 0.5

def f(v, A, B):
    return g-(A/m)*v**B

# Krotka zawierająca początkowe wartości parametrów dopasowania: a i b.
p0 = (0, 0)

# scipy.optimize.curve_fit dokonuje dopasowania.
# p będzie tablicą (ndarray) zawierającą dopasowane parametry.
# pcov będzie tablicą (ndarray) zawierającą macierz kowariancji.
p, pcov = scipy.optimize.curve_fit(f, v, a, p0)


###############################################################################
# Prezentacja danych doświadczalnych i wyników dopasowania.
###############################################################################

# Wypisujemy wyniki na standardowe wyjście.

A, B = p
sigma_A, sigma_B = np.sqrt(np.diag(pcov))

print("Dopasowanie krzywej a(v)")
print(f"   Parametry: {p}")
print(f"   Błędy: {np.sqrt(np.diag(pcov))}")

# Wykreślamy dane doświadczalne wraz z dopasowaniem.
fig, ax = plt.subplots()

ax.grid()
ax.set_xlabel("Prędkość, $v$ [m/s]")
ax.set_ylabel("Przyspieszenie, $a$ [m/s$^2$]")
ax.set_title(fr"Jan Muskat, $A={A:.5f} \pm {sigma_A:.5f}$, $B={B:.2f} \pm {sigma_B:.2f}$")

ax.plot(v, a, "+", color = "red", label = r"Dane doświadczalne")

# p jest tablicą, musimy napisać *p, aby przekazać jej wartości jako niezależne zmienne.
ax.plot(v, f(v, *p), color = "blue", label = r"$a(v)=g-\frac{A}{m}v^B$")

ax.legend()
plt.show()