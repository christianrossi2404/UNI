import numpy as np
import matplotlib.pyplot as plt

# Constantes
L = 16e-6  # Henrios
t = np.linspace(0, 40e-6, 1000)  # Tiempo de 0 a 40 us

# Función de voltaje v(t)
def v(t):
    return np.where(t < 20e-6, 3 * t**2, 1.2e-9)

# Calcular voltaje
v_t = v(t)

# Calcular corriente: i(t) = (1/L) * ∫ v(t) dt
# Usamos integración acumulativa
dt = t[1] - t[0]
i_t = np.cumsum(v_t) * dt / L

# Calcular potencia: p(t) = v(t) * i(t)
p_t = v_t * i_t

# Calcular energía: w(t) = ∫ p(t) dt
w_t = np.cumsum(p_t) * dt

# Graficar
plt.figure(figsize=(10, 8))

# Voltaje
plt.subplot(4, 1, 1)
plt.plot(t * 1e6, v_t * 1e9, 'r')
plt.ylabel('Voltaje (nV)')
plt.title('Voltaje vs. tiempo')
plt.grid()

# Corriente
plt.subplot(4, 1, 2)
plt.plot(t * 1e6, i_t * 1e6, 'b')
plt.ylabel('Corriente (µA)')
plt.title('Corriente vs. tiempo')
plt.grid()

# Potencia
plt.subplot(4, 1, 3)
plt.plot(t * 1e6, p_t * 1e15, 'g')
plt.ylabel('Potencia (fW)')
plt.title('Potencia vs. tiempo')
plt.grid()

# Energía
plt.subplot(4, 1, 4)
plt.plot(t * 1e6, w_t * 1e15, 'm')
plt.xlabel('Tiempo (µs)')
plt.ylabel('Energía (fJ)')
plt.title('Energía acumulada vs. tiempo')
plt.grid()

plt.tight_layout()
plt.show()
