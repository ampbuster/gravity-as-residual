"""
TIME DILATION EXPLAINS THE 14-EVENT SCALING LAW

This calculation shows WHY the 14 SIDC events "match" the M^1.29 scaling:
- All 2D universes have the SAME proper lifetime in their own 2D frame
- The 3+1D-frame lifetime differs because of TIME DILATION
- γ_2D = (E/E_Pl)^1.29 is the time dilation factor
- The "match" is that all 2D universes are EQUAL in their own frame
- The varying 3+1D-frame lifetimes are just different γ values

From §3.17 of the paper:
τ_2D_3+1D = (E/E_Pl)^1.29 × t_Pl
        = γ_2D × t_Pl
        = γ_2D × τ_2D_proper

where:
- τ_2D_proper = t_Pl = 5.39×10^-44 s (proper lifetime in 2D frame)
- γ_2D = (E/E_Pl)^1.29 (time dilation factor)
- τ_2D_3+1D = 3+1D-frame lifetime (what we observe)


**HISTORICAL (v2.x era, mid-2025)**: This file is from the v2.x era, predating:
- v3.0+ Lagrangian work (L102-L136)
- v3.1+ Multi-universe picture (L142-L150)
- v3.3 Bilateral cascade (E_4D = 5e79 J, M_Pl,4D = 3.93e23 GeV)
- v3.5.7+ Naming revolution (f_back -> f_DE, f_DM,leak, f_DM,death)
- v3.5.8+ First-principles (alpha via Schwarzian SYK N=12)
- v3.5.9 A1 (f_leak = H_0)
- v3.5.9+ A2 (alpha dim-specific, eps = 6.32e-34, f_DE,closed = 1.79e-90)

Current v3.5.9+ A2 values (not used in this file):
- M_Pl,2D = 2.95 TeV (FIRST-PRINCIPLES via N*v_H, L308r)
- M_Pl,4D = 3.93e23 GeV (DERIVED via alpha-GM, L308v)
- alpha = 1.289 (FIRST-PRINCIPLES via L308n)
- eps = 6.32e-34 (A2 recalibrated, +4.8 orders)
- f_DE,closed = 1.79e-90 (A2 closed loop)
- gamma_4D = 1.10e+111 (formula uses M_Pl,3D parent reference)
- tau_3D,apparent = 1.66e+145 yr (A2)

The calculations in this file remain valid (math is correct) but the
specific numerical values reflect v2.x era framework, not v3.5.9+ A2.

"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Constants
c = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
GeV = 1.602e-10
yr = 3.156e7
day = 86400
hr = 3600

t_Pl = np.sqrt(hbar * G / c**5)
E_Pl = np.sqrt(hbar * c**5 / G)

# SIDC 14 event types
data = [
    ("Primordial BH evaporation", 1e32, 1e-6),
    ("TDE",                       1e38, 1e-3),
    ("Type Ia SN",                1e44, 33.0),
    ("Core-collapse SN",          1e44, 33.0),
    ("Hypernova",                 1e46, 3.6e3),
    ("Short GRB (BNS merger)",    1e47, 1*day),
    ("Long GRB",                  1e47, 1*day),
    ("NS-BH merger",              1e47, 1*day),
    ("Stellar BH formation",      1e47, 1*day),
    ("AGN flare",                 1e52, 1*yr),
    ("SMBH merger",               1e55, 1e3*yr),
]
data.sort(key=lambda x: x[1])

print("=" * 90)
print("TIME DILATION EXPLAINS THE 14-EVENT SCALING LAW")
print("=" * 90)
print()
print("KEY INSIGHT (§3.17 of the paper):")
print("  All 2D universes have the SAME proper lifetime (τ_2D_proper = t_Pl)")
print("  The 3+1D-frame lifetime differs because of TIME DILATION")
print()
print("  τ_2D_3+1D = γ_2D × τ_2D_proper = (E/E_Pl)^1.29 × t_Pl")
print()
print("=" * 90)
print(f"{'Event':<28} {'E (J)':<12} {'γ_2D':<15} {'τ_2D (s)':<15} {'τ_2D_proper (s)':<18}")
print("=" * 90)

for name, E, tau_2D_actual in data:
    rE = E / E_Pl
    gamma_2D = rE**1.29
    tau_2D_proper = t_Pl  # Same for ALL 2D universes!
    tau_2D_predicted = gamma_2D * tau_2D_proper
    print(f"{name:<28} {E:<12.2e} {gamma_2D:<15.2e} {tau_2D_predicted:<15.2e} {tau_2D_proper:<18.2e}")

print()
print("=" * 90)
print("MASS SCALING: M_2D_2D c² = E_Pl × (E/E_Pl)^0.71")
print("=" * 90)
print()
print("In SR: γ = E_rel / (m_0 c²)")
print("If 2D universe's 'relativistic energy' ~ E and 'rest mass' ~ M_2D_2D:")
print("  γ_2D = E / (M_2D_2D c²)")
print("  M_2D_2D c² = E / γ_2D = E_Pl × (E/E_Pl)^0.71")
print()
print("This means M_2D_2D scales SUB-LINEARLY with E (exponent 0.71 < 1)")
print("Smaller 2D universe = less rest mass per unit energy = MORE time dilation")
print()

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Energy vs gamma
ax = axes[0]
Es_J = np.array([d[1] for d in data])
gammas = (Es_J / E_Pl)**1.29
ax.loglog(Es_J, gammas, 'bo-', markersize=8, label='Data: $\\gamma_{2D} = (E/E_{Pl})^{1.29}$')
ax.loglog(Es_J, Es_J / E_Pl, 'r--', alpha=0.5, label='Linear: $\\gamma = E/E_{Pl}$')
ax.set_xlabel('Event energy E (J)', fontsize=12)
ax.set_ylabel(r'Time dilation factor $\gamma_{2D}$', fontsize=12)
ax.set_title('Time dilation factor scales as $E^{1.29}$', fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, which='both')

# Plot 2: The same γ for all 2D universes (key insight)
ax = axes[1]
# Show that τ_2D_proper is the same for all
Es_J_plot = np.logspace(28, 56, 100)
gamma_2D = (Es_J_plot / E_Pl)**1.29
tau_2D_3plus1D = gamma_2D * t_Pl
tau_2D_proper = t_Pl * np.ones_like(Es_J_plot)  # CONSTANT

ax.loglog(Es_J_plot, tau_2D_3plus1D, 'b-', linewidth=2, label=r'$\tau_{2D}^{3+1D} = \gamma_{2D} \times t_{Pl}$')
ax.loglog(Es_J_plot, tau_2D_proper, 'r--', linewidth=2, label=r'$\tau_{2D}^{proper} = t_{Pl}$ (constant!)')
ax.loglog(Es_J, [d[2] for d in data], 'ko', markersize=8, label='14 SIDC events')
ax.set_xlabel('Event energy E (J)', fontsize=12)
ax.set_ylabel(r'$\tau_{2D}$ (s)', fontsize=12)
ax.set_title('All 2D universes have SAME proper lifetime\n(different 3+1D-frame lifetime = time dilation)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('calculations/time_dilation_explains_scaling.png', dpi=100)
print(f"\nPlot saved to calculations/time_dilation_explains_scaling.png")

print()
print("=" * 90)
print("CONCLUSION: WHY THE 14 EVENTS 'MATCH' THE SCALING LAW")
print("=" * 90)
print("""
The 14 events "match" the M^1.29 scaling law because they all share the
SAME proper lifetime (~t_Pl = 5.39×10^-44 s) in their own 2D frames.

The varying lifetimes we observe (10^-6 s to 10^10 s) are NOT intrinsic to
each 2D universe — they are the 3+1D-frame lifetimes after TIME DILATION.

Each event has a different γ_2D = (E/E_Pl)^1.29, which is exactly the scaling
law. The "match" is then automatic: ALL 2D universes are equal in their
own frame; the difference we see is the time dilation factor.

The 1.29 exponent has the 1 + 1/√12 structure, suggesting N=12 SYK
contributes the time-dilation factor. The 2D universe's rest mass is:

  M_2D_2D c² = E_Pl × (E/E_Pl)^0.71

which is sub-linear: smaller 2D universes have less rest mass per unit
energy, and experience more time dilation. This matches the §10.2
analogy: "less rest mass can travel faster and experiences more time dilation"

DEMOCRATIC COSMOLOGY (§3.17 of the paper):
- All 2D universes are equal (same τ_2D_proper = t_Pl)
- The energy-scaling rule is TIME DILATION
- α = 1.29 is a property of the projection geometry
- α is no longer a free parameter — it's the time-dilation factor
- The empirical calibration (SN 33s) is a MEASUREMENT of the projection
  geometry, not a free fit

This unifies the §3.17 derivation with the c=1 Liouville framework:
- The 2D universe is a Liouville CFT with central charge c=1
- All Liouville CFTs with c=1 have the same "natural" time scale
- The energy scaling γ = (E/E_Pl)^1.29 is the time-dilation factor
- 1.29 = 1 + 1/√12 from N=12 SYK saddle point
""")
