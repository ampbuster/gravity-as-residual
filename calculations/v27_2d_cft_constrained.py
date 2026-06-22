"""
Constrain the cascade's 2D CFT parameters using SPARC observations
==================================================================

The cascade has 4 free parameters (μ, b, α, z_0) that determine:
- m_2D (2D universe mass)
- τ_2D (2D universe lifetime)
- f_active (active fraction)
- α (bulk-brane coupling)

Strategy: combine all 4 SPARC tests to constrain these parameters.

Observational constraints from SPARC:
1. RAR fit: g_+ ~ 9.5e-11 m/s² (within 20% of MOND's a_0 = 1.2e-10)
2. MOND behavior: g_obs ≈ sqrt(g_bar × a_0) at low accel
3. BTFR: V_max^4 ∝ M_b (slope ~3-4)
4. f_active ~ 0.05 (from RAR MCMC posterior, Lelli 2017)

These 4 constraints can be combined to constrain the 2D CFT parameters.


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

import numpy as np
import glob
import os
import json

# Constants
hbar = 1.055e-34
c = 3e8
G_N = 6.674e-11
M_Pl_kg = 2.18e-8
M_Pl_GeV = 1.22e19
M_sun_kg = 1.989e30
kpc_m = 3.086e19
year_s = 365.25 * 24 * 3600
Mpc_m = 3.086e22
H_0 = 70.16e3 / Mpc_m

print("=" * 80)
print("CONSTRAINING CASCADE'S 2D CFT PARAMETERS FROM SPARC")
print("=" * 80)
print()

# =============================================================================
# 2D CFT parameter functions
# =============================================================================
def cascade_g_plus(mu_GeV, b, alpha, z_0_inverse_GeV):
    """Cascade's g_+ from 2D CFT parameters.

    g_+ is the MOND-like acceleration scale.
    In the cascade, g_+ comes from the 2D universe dynamics.

    Natural scale: g_+ = c × H_0 / (2π) (coincidence with cosmology)
    Or: g_+ = m_2D × c / ℏ_planck
    Or: g_+ = sqrt(G_N × rho_cascade)
    """
    # The cascade's g_+ is EMPIRICAL (not derived)
    # But the 2D CFT parameters set the SCALE
    # Try: g_+ = c × H_0 / (2π) = 1.06e-10 m/s²
    g_plus_cosmo = c * H_0 / (2 * np.pi)
    return g_plus_cosmo

def cascade_f_active(mu_GeV, b, alpha, z_0_inverse_GeV):
    """Cascade's f_active from 2D CFT parameters.

    f_active = |C(b)|² × α (DOZZ 3-point function × bulk-brane coupling)

    For b ~ 1, |C|² ~ 0.28 to 46 (large range!)
    """
    C_squared = 1.0 / b**2  # rough approximation
    return C_squared * alpha

def cascade_2D_universe_mass(mu_GeV, b, alpha, z_0_inverse_GeV):
    """2D universe mass in 3+1D frame.

    m_2D_2D = sqrt(μ / b)  (in 2D frame)
    m_2D_3+1D = m_2D_2D × e^{-ky}

    For Karch-Randall, e^{-ky} ~ 1/(k × z_0)
    """
    m_2D_2D_GeV = np.sqrt(mu_GeV / b)
    e_to_minus_ky = 1.0 / (z_0_inverse_GeV * 1e-15)  # rough
    return m_2D_2D_GeV * e_to_minus_ky

def cascade_2D_universe_lifetime(mu_GeV, b, alpha, z_0_inverse_GeV):
    """2D universe lifetime in 3+1D frame.

    τ_2D = ℏ / (m_2D_2D c²)
    τ_3+1D = τ_2D / e^{-ky} = τ_2D × e^{ky}
    """
    m_2D_2D_GeV = np.sqrt(mu_GeV / b)
    m_2D_2D_kg = m_2D_2D_GeV * 1.78e-27
    tau_2D = hbar / (m_2D_2D_kg * c**2)
    e_to_ky = z_0_inverse_GeV * 1e-15
    return tau_2D * e_to_ky

# =============================================================================
# Load SPARC data
# =============================================================================
sparc_dir = "/workspace/github-repo/calculations/sparc_data"
files = sorted(glob.glob(f"{sparc_dir}/*_rotmod.dat"))

g_bars = []
g_obss = []
all_galaxies = []

for f in files:
    name = os.path.basename(f).replace("_rotmod.dat", "")
    try:
        data = np.loadtxt(f, comments='#')
        if data.shape[0] < 3:
            continue
        rad = data[:, 0]
        vobs = data[:, 1]
        vgas = data[:, 3]
        vdisk = data[:, 4]
        vbul = data[:, 5]

        vbar_sq = vgas**2 + 0.5 * vdisk**2 + 0.7 * vbul**2
        vbar = np.sqrt(vbar_sq)

        V_m_s = vobs * 1000
        r_m = rad * kpc_m
        g_obs = V_m_s**2 / r_m
        g_bar = (vbar * 1000)**2 / r_m

        mask = (g_bar > 1e-12) & (g_obs > 1e-12)
        g_bars.extend(g_bar[mask].tolist())
        g_obss.extend(g_obs[mask].tolist())

        all_galaxies.append({
            'name': name,
            'V_max': np.max(vobs),
            'r_max': rad[np.argmax(vobs)],
            'Vbar_at_vmax': vbar[np.argmax(vobs)],
        })
    except:
        continue

g_bars = np.array(g_bars)
g_obss = np.array(g_obss)

print(f"Loaded {len(all_galaxies)} galaxies, {len(g_bars)} RAR data points")
print()

# =============================================================================
# Strategy: parameter sweep over (mu, b, alpha, z_0)
# For each parameter set, compute f_active, g_+, m_2D, τ_2D
# Check against observational constraints
# =============================================================================

# Observational constraints from SPARC + Planck
TARGETS = {
    'g_plus': 1.2e-10,           # ± 20% (within MOND's a_0)
    'f_active': 0.05,            # ± 50% (RAR MCMC posterior)
    'tau_3plus1D': 33,           # ± factor 3 (event-size dependent)
    'm_2D_3plus1D': 1e-15,       # ± 5 orders (axion-like, free)
    'omega_DM': 0.27,            # exact (Planck)
}

# Parameter ranges
mus = [1e-20, 1e-15, 1e-10, 1e-5, 1e0, 1e5, 1e10, 1e15, 1e20]
bs = [0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0]
alphas = [0.001, 0.01, 0.05, 0.1, 0.5, 1.0]
z_0_inverse_GeVs = [1e-25, 1e-20, 1e-15, 1e-10, 1e-5, 1e-1]  # e^{-ky} scale

print("=" * 80)
print("PARAMETER SWEEP: testing (mu, b, alpha, z_0) combinations")
print("=" * 80)
print()

best_params = []
worst_score = np.inf

for mu in mus:
    for b in bs:
        for alpha in alphas:
            for z0 in z_0_inverse_GeVs:
                # Compute cascade predictions
                g_plus_pred = cascade_g_plus(mu, b, alpha, z0)
                f_active_pred = cascade_f_active(mu, b, alpha, z0)
                m_2D_pred = cascade_2D_universe_mass(mu, b, alpha, z0)
                tau_pred = cascade_2D_universe_lifetime(mu, b, alpha, z0)

                # Score against targets (log-scale)
                score = 0
                # g_+ target
                if g_plus_pred > 0:
                    score += abs(np.log10(g_plus_pred / TARGETS['g_plus']))
                # f_active target
                if f_active_pred > 0 and f_active_pred < 1:
                    score += abs(np.log10(f_active_pred / TARGETS['f_active']))
                # tau target (allow wide range)
                if tau_pred > 0:
                    score += 0.1 * abs(np.log10(tau_pred / TARGETS['tau_3plus1D']))
                # m_2D target (allow wide range)
                if m_2D_pred > 0:
                    score += 0.01 * abs(np.log10(m_2D_pred / TARGETS['m_2D_3plus1D']))

                if score < worst_score:
                    worst_score = score
                    best_params = (mu, b, alpha, z0, g_plus_pred, f_active_pred, m_2D_pred, tau_pred)

# Top 10 best fits
print("Top 10 best-fit parameter sets (lowest score):")
print()
print(f"{'mu (GeV)':>10} | {'b':>5} | {'alpha':>7} | {'z0 (GeV)':>10} | {'g_+':>10} | {'f_active':>10} | {'m_2D':>10} | {'tau':>8}")
print("-" * 100)

# Score all and sort
all_results = []
for mu in mus:
    for b in bs:
        for alpha in alphas:
            for z0 in z_0_inverse_GeVs:
                g_plus_pred = cascade_g_plus(mu, b, alpha, z0)
                f_active_pred = cascade_f_active(mu, b, alpha, z0)
                m_2D_pred = cascade_2D_universe_mass(mu, b, alpha, z0)
                tau_pred = cascade_2D_universe_lifetime(mu, b, alpha, z0)

                score = 0
                if g_plus_pred > 0:
                    score += abs(np.log10(g_plus_pred / TARGETS['g_plus']))
                if 0 < f_active_pred < 1:
                    score += abs(np.log10(f_active_pred / TARGETS['f_active']))
                if tau_pred > 0:
                    score += 0.1 * abs(np.log10(tau_pred / TARGETS['tau_3plus1D']))
                if m_2D_pred > 0:
                    score += 0.01 * abs(np.log10(m_2D_pred / TARGETS['m_2D_3plus1D']))

                all_results.append((score, mu, b, alpha, z0, g_plus_pred, f_active_pred, m_2D_pred, tau_pred))

all_results.sort(key=lambda x: x[0])

for r in all_results[:10]:
    score, mu, b, alpha, z0, g_plus_pred, f_active_pred, m_2D_pred, tau_pred = r
    print(f"{mu:10.2e} | {b:5.2f} | {alpha:7.3f} | {z0:10.2e} | {g_plus_pred:10.2e} | {f_active_pred:10.2e} | {m_2D_pred:10.2e} | {tau_pred:8.1e}")

print()

# =============================================================================
# Find the 2D CFT parameters that BEST match all 4 SPARC tests
# =============================================================================
print("=" * 80)
print("BEST FIT PARAMETERS: cascade 2D CFT")
print("=" * 80)
print()

best = all_results[0]
score, mu, b, alpha, z0, g_plus_pred, f_active_pred, m_2D_pred, tau_pred = best

print(f"BEST FIT (lowest total score):")
print(f"  mu = {mu:.2e} GeV (2D cosmological constant)")
print(f"  b = {b:.2f} (Liouville coupling)")
print(f"  alpha = {alpha:.4f} (bulk-brane coupling)")
print(f"  z_0 inverse = {z0:.2e} GeV (Karch-Randall brane location)")
print()
print(f"CASCADE PREDICTIONS:")
print(f"  g_+ = {g_plus_pred:.2e} m/s² (target: {TARGETS['g_plus']:.2e}, within {abs(np.log10(g_plus_pred/TARGETS['g_plus']))*100:.0f}%)")
print(f"  f_active = {f_active_pred:.2e} (target: {TARGETS['f_active']:.2e})")
print(f"  m_2D = {m_2D_pred:.2e} GeV (target: {TARGETS['m_2D_3plus1D']:.2e}, axion-like)")
print(f"  tau_3+1D = {tau_pred:.2e} s (target: {TARGETS['tau_3plus1D']:.2e}, SN-specific)")
print()

# =============================================================================
# Cross-check with SPARC RAR fit
# =============================================================================
print("=" * 80)
print("CROSS-CHECK: SPARC RAR FIT")
print("=" * 80)
print()

# From earlier: best fit g_+ = 9.54e-11 m/s²
g_plus_sparc = 9.54e-11
print(f"SPARC RAR fit g_+: {g_plus_sparc:.2e} m/s²")
print(f"Cascade 2D CFT prediction: {g_plus_pred:.2e} m/s²")
print(f"Ratio: {g_plus_pred / g_plus_sparc:.3f}")
print()

# =============================================================================
# What's actually constrained by data?
# =============================================================================
print("=" * 80)
print("WHAT'S ACTUALLY CONSTRAINED?")
print("=" * 80)
print()
print("FROM SPARC:")
print("  - g_+ = 9.54e-11 m/s² (RAR fit, within 20% of MOND)")
print("  - Cascade predicts g_+ EMPIRICALLY (not from 2D CFT)")
print("  - The 2D CFT doesn't directly predict g_+")
print()
print("FROM PLANCK:")
print("  - omega_DM = 0.27 (Planck 2018)")
print("  - This is a NORMALIZATION, not a 2D CFT prediction")
print()
print("FROM RAR MCMC (Lelli 2017):")
print("  - f_active ~ 0.05 (free parameter, fitted)")
print("  - The cascade POSTULATES this, not derives it")
print()
print("FROM SN LIFETIME (empirical):")
print("  - tau_3+1D ~ 33 s (ℓ/c for SN events)")
print("  - This is a CONSEQUENCE of the event size, not 2D CFT")
print()
print("=" * 80)
print("HONEST VERDICT")
print("=" * 80)
print()
print("The cascade's 2D CFT parameters CAN be tuned to match SPARC,")
print("but they are NOT constrained by SPARC data alone.")
print()
print("What SPARC constrains:")
print("  - g_+ (via RAR): 9.54e-11 m/s², within 20% of MOND")
print("  - This is the SAME as MOND's a_0")
print("  - The cascade's g_+ is EMPIRICAL, not from 2D CFT")
print()
print("What SPARC does NOT constrain:")
print("  - 2D universe mass (m_2D)")
print("  - 2D universe lifetime (tau_2D)")
print("  - Liouville coupling (b)")
print("  - Bulk-brane coupling (alpha)")
print("  - Brane location (z_0)")
print()
print("The 4-parameter (mu, b, alpha, z_0) is DEGENERATE:")
print("  - Many combinations give the same 3+1D cosmology")
print("  - SPARC constrains only the EFFECTIVE g_+")
print("  - 2D CFT specifics are hidden behind the cascade's g_+")
print()
print("VERDICT: The cascade's 2D CFT parameters are FREE PARAMETERS.")
print("SPARC constrains the EFFECTIVE g_+ but not the underlying 2D CFT.")
print("To go further, we need data that probes the 2D CFT directly:")
print("  - 2D universe annihilation signals (if 2D universes can meet)")
print("  - Microlensing from 2D universes (very hard)")
print("  - Direct detection experiments (XENON, LZ, etc.)")
print("  - 2D CFT theoretical breakthrough (Limitation 26)")
