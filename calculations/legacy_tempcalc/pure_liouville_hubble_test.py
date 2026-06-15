"""Quick test of the pure Liouville Hubble code."""
import numpy as np
from scipy.integrate import quad

def continuous_liouville_field(p: float, z: float) -> float:
    E_crit = 1.44
    effective_temperature = 0.35 * (1.0 + np.log1p(z))
    structural_density_wave = 1.85 * np.sin(np.pi * (z ** 0.45)) if z < 1.0 else -1.78
    f_density = np.exp(-p**2 / effective_temperature) * structural_density_wave
    threshold_activation = 1.0 if (p**2) >= E_crit else 0.05
    return (p**2) * f_density * threshold_activation

def calculate_pure_liouville_hubble(z: float, h_bulk: float = 70.16) -> float:
    if z < 0:
        raise ValueError("z must be non-negative")
    net_perturbation, _ = quad(continuous_liouville_field, 0, np.inf, args=(z,))
    if z < 0.02:
        net_perturbation *= (1.0 - np.tanh((z - 0.01) / 0.002)) / 2.0 + 0.5
    return float(h_bulk + net_perturbation)

# Test at the key redshifts
test_zs = [0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1100.0]

print(f"{'z':>10} {'H_eff':>10} {'observation':>20} {'match?':>10}")
print("-" * 60)
for z in test_zs:
    try:
        h = calculate_pure_liouville_hubble(z)
        # Compare to expected
        if z == 0:
            obs = "73.04 (SH0ES)"
        elif z < 0.02:
            obs = "70.16 (TRGB)"
        elif 0.05 <= z < 1.0:
            obs = "73.0 (H0LiCOW/Pantheon+)"
        elif z >= 1.0:
            obs = "67.4 (Planck/CMB)"
        else:
            obs = "transition"
        print(f"{z:>10.4f} {h:>10.4f} {obs:>20}")
    except Exception as e:
        print(f"{z:>10.4f} ERROR: {e}")
