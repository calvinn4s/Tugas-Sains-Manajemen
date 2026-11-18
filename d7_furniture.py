
import numpy as np
from scipy.optimize import minimize

# Fungsi profit
def profit(x):
    x1, x2 = x
    return 6*x1 - 0.1*x1**2 + 8*x2 - 0.2*x2**2

# Karena minimize, profit diberi tanda negatif
def objective(x):
    return -profit(x)

# Constraint: x1 + 2*x2 = 40
def constraint(x):
    return 40 - x[0] - 2*x[1]

# Tebakan awal
initial_guess = [10, 10]

# Optimasi
result = minimize(
    objective,
    initial_guess,
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints={"type": "eq", "fun": constraint}
)

# Hasil
x1, x2 = result.x

print("=" * 40)
print("D7 - FURNITURE OPTIMIZATION")
print("=" * 40)
print("Optimization success:", result.success)
print("Status:", result.message)
print(f"Furniture 1 (x1): {x1:.4f}")
print(f"Furniture 2 (x2): {x2:.4f}")
print(f"Machine hours used: {x1 + 2*x2:.4f}")
print(f"Maximum profit: Rp {profit(result.x):.2f} million")
