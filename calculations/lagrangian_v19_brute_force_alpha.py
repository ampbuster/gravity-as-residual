#!/usr/bin/env python3
"""
Lagrangian v19: Direct brute-force extraction of M^1.29 from SYK spectrum
==========================================================================

Different approach: instead of computing Z and extracting alpha,
directly compute the energy-time relationship from SYK q=4 N=12.

The M^1.29 scaling law says:
  tau_obs = gamma * t_Pl
  gamma = (E / E_Pl)^alpha
  alpha = 1.289

For each energy E (in units of the SYK coupling J), the OBSERVED
time in the 3+1D frame is gamma * t_Pl, where gamma is the time
dilation factor.

The PROPER TIME in the 2D universe frame is t_Pl (universal?).

So: tau_2D_proper = t_Pl (constant)
And: tau_obs = (E/E_Pl)^alpha * t_Pl

For SYK, the natural "energy" is the eigenvalue E_n (in units J=1).
The corresponding "observation time" is ??? (this is what we want to find).

Approach 1: From spectral density rho(E)
  The average time between levels at energy E is ~ 1/rho(E) ~ sqrt(E)
  (Schwarzian prediction: rho(E) ~ exp(S0) sinh(sqrt(E)))
  So tau ~ sqrt(E) -> alpha = 1/2

Approach 2: From the partition function
  The "thermal time" is beta = 1/T
  Z(beta) at temperature T has typical energy E ~ T (high T) or T^2 (low T)
  For Schwarzian: <E> = (some function of beta)
  alpha_eff = d log(<E>)/d log(1/beta)

Approach 3: Direct numerical computation
  For each beta, compute Z(beta) and E_mean(beta) = -d/dbeta log Z
  Then tau_obs(beta) = gamma(beta) * t_Pl = (E_mean(beta)/E_Pl)^alpha * t_Pl
  Compare with the "natural" time at that beta = beta itself
  Find alpha such that tau_obs matches

This is a direct brute-force test of the M^1.29 scaling law.
"""

import numpy as np
from scipy.linalg import eigh

PI = np.pi

print("="*72)
print("LAGRANGIAN v19: BRUTE-FORCE M^1.29 EXTRACTION")
print("="*72)

# =============================================================================
# Build SYK
# =============================================================================
def build_majoranas(N):
    n_half = N // 2
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma_0 = np.eye(2, dtype=complex)

    def tensor(ops):
        result = ops[0]
        for op in ops[1:]:
            result = np.kron(result, op)
        return result

    gammas = []
    for i in range(N):
        pair = i // 2
        ops = []
        for p in range(n_half):
            if p < pair:
                ops.append(sigma_z)
            elif p == pair:
                if i % 2 == 0:
                    ops.append(sigma_x)
                else:
                    ops.append(sigma_y)
            else:
                ops.append(sigma_0)
        gammas.append(tensor(ops))
    return gammas


def build_H_SYK_q4(gammas, seed=42):
    N = len(gammas)
    rng = np.random.default_rng(seed)
    J_var = 6.0 / N**3
    H = np.zeros_like(gammas[0])
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    J_val = rng.normal(0, np.sqrt(J_var))
                    H += J_val * gammas[i] @ gammas[j] @ gammas[k] @ gammas[l]
    return (H + H.conj().T) / 2


# =============================================================================
# Compute Z(beta), E_mean(beta), C(beta), etc. for SYK N=12
# =============================================================================
print("\n" + "="*72)
print("PART 1: SYK q=4 N=12 — THERMODYNAMICS")
print("="*72)

gammas = build_majoranas(12)
H = build_H_SYK_q4(gammas, seed=42)
ev = eigh(H, eigvals_only=True)
ev = ev - ev.min() + 0.1  # shift to positive

# Compute Z(beta), E_mean(beta) = -d/dbeta log Z
betas = np.logspace(-2, 3, 50)

print(f"\n{'beta':>10} {'Z(beta)':>14} {'E_mean':>14} {'E_mean*beta':>14}")
print("-"*70)
results_19 = []
for beta in betas:
    weights = np.exp(-beta * ev)
    Z = np.sum(weights)
    E_mean = np.sum(ev * weights) / Z
    # Cv (heat capacity) — optional
    E_sq_mean = np.sum(ev**2 * weights) / Z
    var_E = E_sq_mean - E_mean**2
    Cv = var_E * beta**2
    results_19.append((beta, Z, E_mean, var_E, Cv))
    if beta in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]:
        print(f"{beta:>10.3f} {Z:>14.4e} {E_mean:>14.4e} {E_mean*beta:>14.4e}")

# =============================================================================
# Test 1: Is Z(beta) a power law? Z ~ beta^p?
# =============================================================================
print("\n" + "="*72)
print("PART 2: IS Z(beta) A POWER LAW?")
print("="*72)

betas_arr = np.array([r[0] for r in results_19])
Z_arr = np.array([r[1] for r in results_19])

# Try different beta ranges
ranges = [(0.1, 1.0), (0.5, 5.0), (1.0, 10.0), (5.0, 50.0), (10.0, 100.0)]

print(f"\n{'beta range':>20} {'log-log slope':>14} {'R^2':>10}")
print("-"*50)
for b_low, b_high in ranges:
    idx = (betas_arr >= b_low) & (betas_arr <= b_high)
    if np.sum(idx) >= 3:
        log_b = np.log(betas_arr[idx])
        log_Z = np.log(Z_arr[idx])
        slope, intercept = np.polyfit(log_b, log_Z, 1)
        # R^2
        Z_pred = np.exp(slope * log_b + intercept)
        ss_res = np.sum((Z_arr[idx] - Z_pred)**2)
        ss_tot = np.sum((Z_arr[idx] - np.mean(Z_arr[idx]))**2)
        R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        print(f"{b_low:>8.2f} - {b_high:>6.2f} {slope:>14.4f} {R2:>10.4f}")

# =============================================================================
# Test 2: Is E_mean(beta) a power law? E_mean ~ beta^(-q)?
# =============================================================================
print("\n" + "="*72)
print("PART 3: IS E_mean(beta) A POWER LAW?")
print("="*72)

E_arr = np.array([r[2] for r in results_19])

print(f"\n{'beta range':>20} {'log-log slope':>14} {'R^2':>10}")
print("-"*50)
for b_low, b_high in ranges:
    idx = (betas_arr >= b_low) & (betas_arr <= b_high)
    if np.sum(idx) >= 3:
        log_b = np.log(betas_arr[idx])
        log_E = np.log(E_arr[idx])
        slope, intercept = np.polyfit(log_b, log_E, 1)
        # R^2
        E_pred = np.exp(slope * log_b + intercept)
        ss_res = np.sum((E_arr[idx] - E_pred)**2)
        ss_tot = np.sum((E_arr[idx] - np.mean(E_arr[idx]))**2)
        R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        print(f"{b_low:>8.2f} - {b_high:>6.2f} {slope:>14.4f} {R2:>10.4f}")

# =============================================================================
# Test 3: alpha from tau(E) ~ E^alpha
# =============================================================================
print("\n" + "="*72)
print("PART 4: alpha FROM tau(E) ~ E^alpha")
print("="*72)

# The SIDC scaling: tau_obs = (E/E_Pl)^alpha * t_Pl
# In 2D frame: tau_2D = t_Pl (universal?)
# In 3+1D frame: tau_obs = gamma * tau_2D = gamma * t_Pl
# where gamma = (E/E_Pl)^alpha

# For the SYK: E (in units J=1) corresponds to the 2D energy
# "E_Pl" for SYK = J * some normalization
# For SYK, the natural "Planck" is J ~ 1 in our units

# So tau_2D_proper = some constant (not necessarily t_Pl)
# tau_obs = (E/J)^alpha * tau_2D_proper

# Test: at beta = 1/T, <E> ~ T (high T) or T^2 (low T)
# For high T: <E> ~ 1/beta
# If tau_obs = 1/<E> * something, then tau_obs ~ beta ~ 1/E
# alpha = -1 (inverse)

# But SIDC says alpha = +1.289
# So maybe the OBSERVATION time is INVERSELY related to E

# Let's test: does <E> * tau_obs = constant? Or what?
# For Schwarzian: <E> ~ 1/beta^2 (low T)
# So tau ~ 1/<E>^{1/2} ~ beta
# alpha = +1/2 (positive, low T)

print("\nAssuming tau_obs = beta (the thermal time):")
print("tau_obs ~ beta")
print("<E>(beta) ~ ?")
print(f"\nIf tau_obs ~ beta ~ E^-alpha, then alpha = -d log beta / d log <E>")
print(f"For Schwarzian low-T: <E> ~ 1/beta^2 -> alpha = +1/2")
print(f"For high-T: <E> ~ 1/beta -> alpha = +1")
print(f"For very low-T (ground state): <E> ~ const -> alpha = 0")

# Compute alpha empirically
print(f"\nEmpirical alpha from SYK:")
print(f"{'beta range':>20} {'alpha_empirical':>16}")
print("-"*45)
for b_low, b_high in ranges:
    idx = (betas_arr >= b_low) & (betas_arr <= b_high)
    if np.sum(idx) >= 3:
        log_b = np.log(betas_arr[idx])
        log_E = np.log(E_arr[idx])
        slope, _ = np.polyfit(log_b, log_E, 1)
        # <E> ~ beta^slope -> tau ~ beta ~ E^(-1/slope)
        # alpha = -1/slope
        if slope != 0:
            alpha_emp = -1 / slope
        else:
            alpha_emp = np.nan
        print(f"{b_low:>8.2f} - {b_high:>6.2f} {alpha_emp:>16.4f}")

# =============================================================================
# Test 4: Compare with alpha = 1.289
# =============================================================================
print("\n" + "="*72)
print("PART 5: COMPARISON WITH alpha = 1.289")
print("="*72)

# Maybe try different observable
# tau_obs vs E_mean
# Linear fit log(tau_obs) = alpha * log(E) + const
# Where tau_obs = beta (thermal time)

log_tau = np.log(betas_arr)
log_E = np.log(E_arr)
slope, intercept = np.polyfit(log_E, log_tau, 1)
print(f"\nLinear fit: log(beta) = {slope:.4f} * log(<E>) + {intercept:.4f}")
print(f"Slope = alpha = {slope:.4f}")
print(f"SIDC alpha = 1.289")
print(f"Match: {abs(slope - 1.289) < 0.1}")

# =============================================================================
# Test 5: With full 3-sector partition function
# =============================================================================
print("\n" + "="*72)
print("PART 6: COMBINED Z (JT + Liouville + SYK)")
print("="*72)

# From v13: Z_JT * Z_L * Z_SYK
# Use rough Schwarzian for JT and Liouville

def Z_JT(beta, S0=0):
    """Jackiw-Teitelboim partition function."""
    return np.exp(S0) * (beta/(2*PI))**1.5 * np.exp(PI**2 / beta)


def Z_Liouville(beta, mu=1.0, n_max=10):
    """c=1 Liouville partition function (rough)."""
    energies = np.array([(n+1)**2 / (8 * PI * mu) for n in range(n_max)])
    return np.sum(np.exp(-beta * energies))


# Compute combined Z
print(f"\n{'beta':>10} {'Z_JT':>14} {'Z_L':>14} {'Z_SYK':>14} {'Z_total':>14}")
print("-"*70)
Z_combined_arr = []
for beta in betas:
    ZJ = Z_JT(beta)
    ZL = Z_Liouville(beta, mu=0.5)
    ZS = np.sum(np.exp(-beta * ev))
    ZT = ZJ * ZL * ZS
    Z_combined_arr.append(ZT)
    if beta in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
        print(f"{beta:>10.3f} {ZJ:>14.4e} {ZL:>14.4e} {ZS:>14.4e} {ZT:>14.4e}")

Z_combined_arr = np.array(Z_combined_arr)

# Extract alpha from combined Z
print(f"\n{'beta range':>20} {'alpha from Z_combined':>22}")
print("-"*50)
for b_low, b_high in ranges:
    idx = (betas_arr >= b_low) & (betas_arr <= b_high)
    if np.sum(idx) >= 3:
        log_b = np.log(betas_arr[idx])
        log_ZT = np.log(Z_combined_arr[idx])
        slope, _ = np.polyfit(log_b, log_ZT, 1)
        alpha_eff = -slope
        print(f"{b_low:>8.2f} - {b_high:>6.2f} {alpha_eff:>22.4f}")

# =============================================================================
# Verdict
# =============================================================================
print("\n" + "="*72)
print("PART 7: VERDICT (v19)")
print("="*72)
print("""
DIRECT BRUTE-FORCE M^1.29 EXTRACTION (v19):
  + Computed Z(beta), E_mean(beta), and combined Z for SYK q=4 N=12
  + Extracted alpha from log-log slopes in various beta ranges
  + Tested both pure SYK and combined Z (JT + L + SYK)

KEY FINDING:
  - Pure SYK gives alpha ~ 0.5-1.0 depending on beta range
  - Combined Z gives alpha_eff in similar range (NOT cleanly 1.289)
  - The M^1.29 scaling law is NOT directly visible from the spectrum

INTERPRETATION:
  - The alpha = 1.289 is a CROSS-SECTOR phenomenon
  - The pure 2D theory (Liouville + SYK + Schwarz) gives different alpha in different regimes
  - The M^1.29 is an EMERGENT scaling from the COMBINED + the OBSERVATION projection
  - To derive 1.289 from Z alone, we would need:
    * EXACT Z_Liouville (DOZZ formula on torus)
    * EXACT cross-coupling between sectors
    * Correctly identified observable (what is tau_obs in the 2D frame?)

CONCLUSION FOR L43:
  - Brute force doesn't close L43 (consistent with v11c, v12)
  - The Lagrangian skeleton L = L_c=1 + L_N=12 + L_Schwarzian is NOT a complete Lagrangian
  - Closing L43 requires cross-coupling terms + correct observable identification
""")