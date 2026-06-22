"""
Cascade lifespan v2: 33s is for a SPECIFIC supernova, scales with event energy.


**HISTORICAL (v2.7 era, mid-2025)**: This file is from the v2.7.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back → f_DE,f_DM,leak,f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N×v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via α-GM, L308v)
- α = 1.289 (FIRST-PRINCIPLES via L308n)
- ε = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- γ_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- τ_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.7 era framework, not v3.5.9+ A2.
"""
import math

# Constants
c = 2.998e8
hbar = 1.055e-34
G_N = 6.674e-11
year = 3.156e7

# 3+1D Planck
t_Pl_3 = math.sqrt(hbar * G_N / c**5)
E_Pl_3 = math.sqrt(hbar * c**5 / G_N)

# Calibration point: 33s is for a Type Ia supernova
E_Type_Ia = 1e44   # J
T_Type_Ia_2D = 33  # s

# Calibrate alpha
alpha = math.log(T_Type_Ia_2D / t_Pl_3) / math.log(E_Type_Ia / E_Pl_3)
print("="*72)
print(" ENERGY-SCALING RULE:  T_{D-1} = t_Pl,3 × (E_D / E_Pl,3)^α")
print(" Calibrated: 33 s  ↔  10^44 J (Type Ia supernova)")
print(f" Best-fit α  =  {alpha:.3f}")
print("="*72)

# Lifespans for various 3D events (energies in joules)
events = [
    ("Volcanic eruption (Mt)", 1e18),
    ("Tunguska-class impact", 1e17),
    ("Tornado", 1e15),
    ("TNT ton equivalent", 4e9),
    ("Solar flare (X-class)", 1e25),
    ("Earthquake (M9)", 1e17),
    ("Small nova", 1e34),
    ("Bright nova (M31)", 1e35),
    ("Type Ia supernova", 1e44),
    ("Hypernova (slSN)", 1e46),
    ("Long GRB (on-axis)", 1e47),
    ("Short GRB", 1e45),
    ("Magnetar giant flare", 1e40),
    ("BNS merger (GW170817)", 1e53),
    ("AGN flare (blazar)", 1e55),
    ("Quasar outburst", 1e60),
    ("Total AGN power × 10^8 yr", 1e62),
]

print()
print(f"{'Event':35s} {'Energy (J)':>12s}  {'2D universe lifespan':>25s}")
print("-"*72)
for name, E in events:
    T = t_Pl_3 * (E / E_Pl_3) ** alpha
    if T < 1e-3:
        ts = f"{T*1e6:.2e} μs"
    elif T < 1:
        ts = f"{T*1e3:.2e} ms"
    elif T < 60:
        ts = f"{T:.2f} s"
    elif T < 3600:
        ts = f"{T/60:.2f} min"
    elif T < 86400:
        ts = f"{T/3600:.2f} hr"
    elif T < 31557600:
        ts = f"{T/86400:.2f} days"
    elif T < 31557600 * 100:
        ts = f"{T/year:.2f} yr"
    else:
        ts = f"{T/year:.2e} yr"
    print(f"  {name:33s} {E:>12.1e}  {ts:>25s}")

# 4D cosmological event
print()
print("="*72)
print(" 4D COSMOLOGICAL EVENT → 3D UNIVERSE (us)")
print("="*72)

E_4D = 1e69   # J (rest energy of observable 3+1D universe)
E_4D_total = 1e72  # J (full 4D event including 4D's own degrees of freedom)

for label, E in [("Rest energy of observable 3D universe", E_4D),
                 ("Full 4D cosmological event (estimate)", E_4D_total)]:
    T_3D = t_Pl_3 * (E / E_Pl_3) ** alpha
    print(f"\n  {label}: E = {E:.1e} J")
    print(f"    T_3D in 4D frame = {T_3D:.2e} s")
    print(f"                      = {T_3D/year:.2e} yr")
    print(f"                      = {T_3D/year/1e9:.2e} Gyr")
    print(f"                      = {T_3D/year/1e12:.2e} Tyr (terayears)")
    print(f"    In 4D Planck times (t_Pl,4 = t_Pl,3): {T_3D/t_Pl_3:.2e}")

# Comparison: how does 33s scale with E for the cascade's downward 2D universe?
print()
print("="*72)
print(" 3D's INTERNAL lifespan T_3D' (the 3D's own clock)")
print("="*72)
print("  T_3D' = T_3D in 4D × (time-dilation factor)")
print()
print("  Time-dilation factor depends on ratio of 4D Planck time to 3D Planck time.")
print("  Two scenarios:")

T_3D_internal_no_dilation = 1.9e26  # yr (from above, no time-dilation)
T_3D_current = 13.8e9              # yr (current age)
print(f"\n  Scenario 1: t_Pl,4 ~ t_Pl,3 (no extra time-dilation)")
print(f"    T_3D' ~ 2 × 10^26 yr = {T_3D_internal_no_dilation:.2e} yr")
print(f"    Current age (13.8 Gyr) / total lifespan: {T_3D_current/T_3D_internal_no_dilation:.2e} ({T_3D_current/T_3D_internal_no_dilation*100:.2e}%)")
print(f"    DE constant over 10^26 yr  →  consistent with current observations")
print(f"    DESI evolving DE (3.5σ)  →  first probe of T_3D'")
print()

print(f"  Scenario 2: t_Pl,4 = t_Pl,3 / 10^26 (4D clock 10^26× faster)")
T_3D_internal_big_dilation = T_3D_internal_no_dilation * 1e26
print(f"    T_3D' ~ 2 × 10^52 yr = {T_3D_internal_big_dilation:.2e} yr")
print(f"    Current age / total lifespan: {T_3D_current/T_3D_internal_big_dilation:.2e} ({T_3D_current/T_3D_internal_big_dilation*100:.2e}%)")
print(f"    Implies M_Pl,4 ~ 10^45 GeV (unphysical — beyond Planck scale)")
print()

# ===========================================================================
# DE TIME-DILATION: why DE is constant over 3D's lifespan
# ===========================================================================
print("="*72)
print(" DE TIME-DILATION:  Why is DE roughly constant?")
print("="*72)
print("  The 4D's gravity, projected into 3D, appears 'frozen' because the")
print("  3D's clock is too slow to resolve the 4D's fast dynamics.")
print()
print("  For DE to be roughly constant:  T_3D lifespan  >>  4D's dynamical time")
print()
print("  If 4D dynamical time = 4D Planck time = t_Pl,4:")
print(f"    Required:  T_3D' / t_Pl,4  ≳  10^10  (10 billion × freezing)")
print()
T_3D_lifespan_yr = 1.9e26
T_3D_lifespan_s = T_3D_lifespan_yr * year
print(f"  Assuming T_3D' = 2 × 10^26 yr = {T_3D_lifespan_s:.2e} s:")
print(f"    Required t_Pl,4 ≤ T_3D' / 10^10 = {T_3D_lifespan_s/1e10:.2e} s")
print(f"    = {T_3D_lifespan_s/1e10/t_Pl_3:.2e} × t_Pl,3")
print()
print("  This means t_Pl,4 can be COMPARABLE to t_Pl,3 (no extreme fine-tuning!)")
print("  The 3D's lifespan is so much longer than the 4D's Planck time that")
print("  DE appears constant even without extreme Planck-time ratios.")
print()
print("  Conclusion:  with energy scaling, DE is naturally constant over")
print("               the 3D's ~10^26-yr lifespan, no extreme fine-tuning needed.")
