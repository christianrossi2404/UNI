import numpy as np
import matplotlib.pyplot as plt

# Parámetros
L = 0.05  # Henrios

# Tiempo
t = np.linspace(-2, 15, 1000)
dt = t[1] - t[0]

# Definimos i(t) por tramos con funciones y constantes
def i_func(t):
    return np.piecewise(
        t,
        [t < 0,
         (t >= 0) & (t < 2),
         (t >= 2) & (t < 6),
         t >= 6],
        [lambda t: 15,
         lambda t: 15,
         lambda t: -10/4*t + 20,
         5]
    )

# Corriente
i = i_func(t)

# Derivada numérica (di/dt)
di_dt = np.gradient(i, dt)

# Tensión v(t) = L * di/dt
v = L * di_dt

# Potencia p(t) = v(t) * i(t)
p = v * i

# Energía acumulada
E = np.cumsum(p) * dt

# === Gráficos ===
plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.plot(t, i, label="Corriente i(t)")
plt.ylabel("i(t) [A]")
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, v, label="Tensión v(t)", color='red')
plt.ylabel("v(t) [V]")
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, p, label="Potencia p(t)", color='green')
plt.ylabel("p(t) [W]")
plt.grid(True)
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, E, label="Energía acumulada E(t)", color='purple')
plt.ylabel("E(t) [J]")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
