
import numpy as np
from scipy.optimize import minimize

# Data toko: (x, y, weight)
stores = [
    (2, 8, 20),
    (6, 2, 10),
    (8, 6, 30),
    (3, 3, 15)
]

# Fungsi total weighted distance
def objective(location):
    x, y = location
    total = 0

    for sx, sy, weight in stores:
        distance = np.sqrt((x - sx)**2 + (y - sy)**2)
        total += weight * distance

    return total

# Tebakan awal
initial_guess = [5, 5]

# Optimasi
result = minimize(
    objective,
    initial_guess,
    method="Nelder-Mead",
    bounds=[(0, None), (0, None)],
    options={"xatol": 1e-9, "fatol": 1e-9}
)

# Hasil
x, y = result.x

print("=" * 45)
print("D8a - WAREHOUSE LOCATION OPTIMIZATION")
print("=" * 45)
print("Optimization success:", result.success)
print("Status:", result.message)
print(f"Optimal X coordinate: {x:.6f}")
print(f"Optimal Y coordinate: {y:.6f}")
print(f"Minimum weighted distance: {result.fun:.6f}")
