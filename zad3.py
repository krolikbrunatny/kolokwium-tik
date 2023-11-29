import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funkcja modelująca
def model(x, a, b, c, d):
    return a * x + b * x**3 + c * np.exp(d * x)

data = np.loadtxt('data2.txt', unpack=True)

# Extract the columns from the data
x_data = data[0]
y_data = data[1]
y_err = data[2]

# Dopasowanie krzywej do danych z uwzględnieniem niepewności
popt, pcov = curve_fit(model, x_data, y_data, sigma=y_err)
a, b, c, d = popt
a_err, b_err, c_err, d_err = np.sqrt(np.diag(pcov))

# Zakres dla krzywej
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = model(x_fit, *popt)

# Tworzenie wykresu
plt.errorbar(x_data, y_data, yerr=y_err, fmt='o', color='orange', label='Pomiary z niepewnościami')
plt.plot(x_fit, y_fit, color='green', linestyle='-', label='Dopasowana krzywa')

# Dodanie tytułu, etykiet osi i legendy
plt.title(f'Wyniki pomiarów - Imię i Nazwisko\na = {a:.2f} ± {a_err:.2f}, b = {b:.2f} ± {b_err:.2f}, c = {c:.2f} ± {c_err:.2f}, d = {d:.2f} ± {d_err:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Zapis do pliku
# plt.savefig('/mnt/data/zad3.pdf')

plt.show()