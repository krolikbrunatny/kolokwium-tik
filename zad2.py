import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funkcja modelująca
def model(v, A, B):
    g = 9.8  # stała grawitacyjna w m/s^2
    return g - (A / v**B)

data = np.loadtxt('data1.txt', unpack=True)

# Extract the columns from the data
v_data = data[0]
a_data = data[1]

# Dopasowanie krzywej do danych
popt, pcov = curve_fit(model, v_data, a_data)
A, B = popt
A_err, B_err = np.sqrt(np.diag(pcov))

# Zakres dla krzywej
v_fit = np.linspace(min(v_data), max(v_data), 100)
a_fit = model(v_fit, *popt)

# Tworzenie wykresu
plt.plot(v_fit, a_fit, color='blue', linestyle='-', label='Dopasowana krzywa: a(v)')
plt.scatter(v_data, a_data, color='red', marker='x', label='Pomiary')

# Dodanie tytułu, etykiet osi i legendy
plt.title(f'Wyniki pomiarów - Imię i Nazwisko\nA = {A:.2f} ± {A_err:.2f}, B = {B:.2f} ± {B_err:.2f}')
plt.xlabel('Prędkość v (m/s)')
plt.ylabel('Przyspieszenie a (m/s^2)')
plt.legend()

# Zapis do pliku
# plt.savefig('/mnt/data/zad2.pdf')

plt.show()