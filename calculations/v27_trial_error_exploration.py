"""
TRIAL-AND-ERROR exploration of the energy-scaling rule.
Map the cascade's T_{D-1} = 33s × (E / 10^44 J)^alpha rule to MANY points
and try several exponents to see which is most cascade-consistent.
"""
import math

# Constants
t_Pl = 5.39e-44  # s
E_Pl = 1.96e9    # J
year = 3.156e7   # s

# Calibration
E_SN = 1e44      # J
T_SN = 33        # s
alpha_best = math.log(T_SN / t_Pl) / math.log(E_SN / E_Pl)
print(f"="*78)
print(f" BEST-FIT alpha: {alpha_best:.4f}")
print(f"="*78)

def T_lifetime(E, alpha):
    """Power-law rule: T = t_Pl × (E / E_Pl)^alpha"""
    return t_Pl * (E / E_Pl) ** alpha

# Try several candidate exponents
candidates = {
    "α=0  (constant)":      0.0,
    "α=1/3 (cube root)":     1/3,
    "α=1/2 (square root)":   0.5,
    "α=2/3":                 2/3,
    "α=1   (linear)":        1.0,
    "α=4/3 (Bondi-like)":    4/3,
    f"α={alpha_best:.3f} (best fit)":  alpha_best,
    "α=3/2":                 1.5,
    "α=2   (quadratic)":     2.0,
    "α=5/2":                 2.5,
}

# Map E from 1 J to 10^85 J (54 decades wider than before)
print()
print("="*78)
print(" WIDE-RANGE ENERGY-SCALING TABLE — predicted 2D universe lifetime")
print("="*78)
print(f"  Calibration point:  Type Ia SN  (E=10^44 J)  →  33 s")
print()

# Display every 2 decades of energy
print(f"{'E (J)':>8s} {'log10 E':>8s} | " + " | ".join(f"{name:>17s}" for name in candidates))
print("-"*78)

events = [
    1, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 1e30,
    1e33, 1e36, 1e39, 1e42, 1e44, 1e47, 1e50, 1e53, 1e56, 1e60,
    1e65, 1e69, 1e72, 1e75, 1e80,
]

def fmt_time(T):
    if T < 1e-15:
        return f"{T*1e18:.2e} as"
    elif T < 1e-12:
        return f"{T*1e15:.2e} fs"
    elif T < 1e-9:
        return f"{T*1e12:.2e} ps"
    elif T < 1e-6:
        return f"{T*1e9:.2e} ns"
    elif T < 1e-3:
        return f"{T*1e6:.2e} μs"
    elif T < 1:
        return f"{T*1e3:.2e} ms"
    elif T < 60:
        return f"{T:.2f} s"
    elif T < 3600:
        return f"{T/60:.2f} min"
    elif T < 86400:
        return f"{T/3600:.2f} hr"
    elif T < 31557600:
        return f"{T/86400:.2f} days"
    elif T < 31557600 * 100:
        return f"{T/year:.2e} yr"
    elif T < 31557600 * 1e9:
        return f"{T/year/1e6:.2e} Myr"
    else:
        return f"{T/year/1e9:.2e} Gyr"

for E in events:
    times = [fmt_time(T_lifetime(E, alpha)) for alpha in candidates.values()]
    print(f"{E:>8.1e} {math.log10(E):>8.1f} | " + " | ".join(f"{t:>17s}" for t in times))

# ===========================================================================
# Find what energy corresponds to specific (D-1)-universe lifetimes
# ===========================================================================
print()
print("="*78)
print(" INVERSE PROBLEM:  what E gives a specific 2D universe lifetime?")
print("="*78)
print(f"  (For the cascade's best-fit α = {alpha_best:.4f})")
print()

target_lifetimes = [
    ("1 Planck time (t_Pl)", t_Pl),
    ("1 attosecond", 1e-18),
    ("1 femtosecond", 1e-15),
    ("1 nanosecond", 1e-9),
    ("1 microsecond", 1e-6),
    ("1 millisecond", 1e-3),
    ("1 second", 1),
    ("33 seconds (SN calibration)", 33),
    ("1 hour", 3600),
    ("1 day", 86400),
    ("1 year", year),
    ("100 years", 100 * year),
    ("Hubble time (~14 Gyr)", 14e9 * year),
    ("1 T_yr = 10^12 yr", 1e12 * year),
    ("1 E_yr = 10^18 yr", 1e18 * year),
    ("cascade 2×10^26 yr (4D view of 3D)", 2e26 * year),
]

print(f"{'Target 2D lifetime':>40s} | {'Required E (J)':>20s} | {'Physical event':>30s}")
print("-"*100)
for label, T in target_lifetimes:
    # Solve T = t_Pl × (E/E_Pl)^alpha  for E
    E_needed = E_Pl * (T / t_Pl) ** (1/alpha_best)
    # Identify the event
    if E_needed < 1e6:
        event = "chemical reaction"
    elif E_needed < 1e9:
        event = "small explosion"
    elif E_needed < 1e12:
        event = "1 ton TNT"
    elif E_needed < 1e15:
        event = "Mt-class eruption"
    elif E_needed < 1e25:
        event = "Tunguska-class impact"
    elif E_needed < 1e35:
        event = "solar flare / small nova"
    elif E_needed < 1e40:
        event = "magnetar giant flare"
    elif E_needed < 1e45:
        event = "Type Ia supernova (calibration)"
    elif E_needed < 1e50:
        event = "hypernova / GRB"
    elif E_needed < 1e55:
        event = "BNS merger"
    elif E_needed < 1e60:
        event = "AGN flare / quasar"
    elif E_needed < 1e65:
        event = "AGN total output × 10 Myr"
    elif E_needed < 1e72:
        event = "4D cosmological event (rest energy of 3D)"
    else:
        event = "5D+ cosmological event"
    print(f"{label:>40s} | {E_needed:>20.2e} | {event:>30s}")

# ===========================================================================
# Self-similarity check:  what is the same 33s-rule going UP the ladder?
# ===========================================================================
print()
print("="*78)
print(" UPWARD LADDER:  what does the rule say for 4D, 5D, 6D cosmological events?")
print("="*78)
print()
print("  If we assume E_5D ~ 10^25 × E_4D, E_6D ~ 10^25 × E_5D, etc. (cascade's")
print("  self-similar energy scaling), then the 4D's, 5D's, etc. universes have:")
print()

E_D_values = {
    "3D (us)":              1e69,
    "4D universe":          1e69 * 1e25,
    "5D universe":          1e69 * (1e25)**2,
    "6D universe":          1e69 * (1e25)**3,
    "7D universe":          1e69 * (1e25)**4,
}

print(f"{'Dimension':>15s} | {'E (J)':>15s} | {'Lifetime in next-up view':>30s} | {'In next-up Planck times':>25s}")
print("-"*100)
for label, E in E_D_values.items():
    T = T_lifetime(E, alpha_best)
    t_Pl_up = t_Pl  # assume next-up Planck time ~ 3D Planck time
    n_Pl = T / t_Pl_up
    print(f"{label:>15s} | {E:>15.2e} | {T/year:>25.2e} yr | {n_Pl:>25.2e}")

print()
print("="*78)
print(" SUMMARY:  the energy-scaling ladder at α=1.29 spans 65+ orders of magnitude")
print("="*78)
print(f"  Smallest event (1 J)                  →  2D universe lifetime = {T_lifetime(1, alpha_best):.2e} s")
print(f"  Calibration (Type Ia SN, 10^44 J)     →  2D universe lifetime = 33 s")
print(f"  Largest 2D-event (quasar, 10^60 J)    →  2D universe lifetime = {T_lifetime(1e60, alpha_best)/year:.2e} yr")
print(f"  4D cosmological event (10^69 J)       →  3D universe (us) in 4D view = {T_lifetime(1e69, alpha_best)/year:.2e} yr")
print(f"  5D cosmological event (~10^94 J)      →  4D universe in 5D view = {T_lifetime(1e94, alpha_best)/year:.2e} yr")
print(f"  6D cosmological event (~10^119 J)     →  5D universe in 6D view = {T_lifetime(1e119, alpha_best)/year:.2e} yr")
