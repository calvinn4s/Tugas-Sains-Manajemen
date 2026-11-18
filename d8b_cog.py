
import numpy as np

# Data toko: (x, y, weight)
stores = np.array([
    [2, 8, 20],
    [6, 2, 10],
    [8, 6, 30],
    [3, 3, 15]
])

x = stores[:, 0]
y = stores[:, 1]
w = stores[:, 2]

# Menghitung Center of Gravity
xc = np.sum(w * x) / np.sum(w)
yc = np.sum(w * y) / np.sum(w)

# Menghitung weighted distance pada lokasi CoG
total_distance = 0

for sx, sy, weight in stores:
    distance = np.sqrt((xc - sx)**2 + (yc - sy)**2)
    total_distance += weight * distance

print("=" * 45)
print("D8b - CENTER OF GRAVITY")
print("=" * 45)
print(f"Total weight: {np.sum(w):.2f}")
print(f"Center X: {xc:.6f}")
print(f"Center Y: {yc:.6f}")
print(f"Weighted distance: {total_distance:.6f}")
