import math
import matplotlib.pyplot as plt
import numpy as np

K = 15000000000
N0 = 1000000

# Variar A
A_values = np.linspace(1, 10, 100)
a_values_A = [(math.log((K / N0) - 1) - math.log(A)) / 1 for A in A_values]

# Variar t
t_values = np.linspace(1, 10, 100)
a_values_t = [(math.log((K / N0) - 1) - math.log(1)) / t for t in t_values]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(A_values, a_values_A)
plt.xlabel('A')
plt.ylabel('a')
plt.title('Comportamiento de a al variar A')

plt.subplot(1, 2, 2)
plt.plot(t_values, a_values_t)
plt.xlabel('t')
plt.ylabel('a')
plt.title('Comportamiento de a al variar t')

plt.tight_layout()
plt.show()