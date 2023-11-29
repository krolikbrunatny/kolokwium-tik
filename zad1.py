import matplotlib.pyplot as plt
import numpy as np

# Definicje funkcji
def f_1(x):
    return 1/3 * np.sin(3 * x)

def f_2(x):
    return 1/5 * np.sin(5 * x)

def f_3(x):
    return 1/9 * np.sin(9 * x)

# Zakres wartości x
x = np.linspace(-1, 3, 400)

# Tworzenie wykresów funkcji
plt.plot(x, f_1(x), color='yellow', linestyle='-', label=r'$f_1(x) = \frac{1}{3}\sin(3x)$')
plt.plot(x, f_2(x), color='red', linestyle='--', label=r'$f_2(x) = \frac{1}{5}\sin(5x)$')
plt.plot(x, f_3(x), color='blue', linestyle=':', label=r'$f_3(x) = \frac{1}{9}\sin(9x)$')

# Dodanie linii siatki, tytułu, etykiet osi i legendy
plt.grid(True)
plt.title('Wykresy funkcji - Imię i Nazwisko')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.legend()

# Zapis do pliku
plt.savefig('zad1.pdf')

plt.show()