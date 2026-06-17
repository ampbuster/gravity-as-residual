#!/usr/bin/env python3
"""
Lagrangian v18: Replica trick for f_back
==========================================

The replica trick computes the von Neumann entropy:
S = -d/dn log Z_n |_{n=1}

where Z_n is the partition function on an n-fold cover of the
original geometry.

For the 2D universe in SIDC:
- Geometry: 2D disc with boundary = the 3+1D brane
- n-fold cover: n discs connected at the boundary
- Z_n = integral exp(-S_n) over all configurations on the cover

For the SYK q=4 sector, Z_n can be computed exactly via diagonalization.
The entropy S(E) gives us information about the 2D universe.

Approach:
1. Build the n-fold cover partition function Z_n(beta) for n = 1, 2, 3, ..., 10
2. Compute log Z_n as a function of n
3. Numerically differentiate: S = -d/dn log Z_n |_{n=1}
4. Compare with the 2D universe entropy (e.g., Bekenstein-Hawking)

For the COMBINED theory (Liouville + SYK):
- Z_n_combined = Z_n_Liouville * Z_n_SYK
- Liouville replica: well-studied (gives log corrections)
- SYK replica: known from the SYK literature

We test:
1. Does S(E) ~ log(E) (as expected for 2D CFT)?
2. Is f_back derivable from S(E)?
"""

import numpy as np
from scipy.linalg import eigh

PI = np.pi

print("="*72)
print("LAGRANGIAN v18: REPLICA TRICK FOR f_back")
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
# Replica partition function
# =============================================================================
# For an n-fold cover, the Hilbert space is n copies of the original
# So Z_n = Tr(exp(-beta H)) where H is the SAME H but traced over n copies
#
# More precisely: Z_n(beta) = Tr( exp(-beta H_tot) )
# where H_tot = sum_{a=1}^n H_a (n identical copies)
# Since copies don't interact: H_tot eigenvalues = sum of n copies of H eigenvalues
# Z_n(beta) = sum over eigenvalue sums

def Z_replica(ev, beta, n_replica):
    """Compute Z_n(beta) for an n-fold replica of the system."""
    # For non-interacting replicas: H_tot eigenvalues = sum of n copies of H eigenvalues
    # Z_n(beta) = sum_{i_1, ..., i_n} exp(-beta (E_{i_1} + ... + E_{i_n}))
    #          = sum_{i_1} exp(-beta E_{i_1}) ... sum_{i_n} exp(-beta E_{i_n})
    #          = (Z_1(beta))^n
    # This is for NON-INTERACTING replicas
    Z_1 = np.sum(np.exp(-beta * ev))
    return Z_1 ** n_replica


def entropy_replica(ev, beta):
    """Compute von Neumann entropy via replica trick.

    For non-interacting replicas, this is exactly zero.
    We need INTERACTING replicas for nontrivial entropy.
    """
    # Try: entropy from the density of states
    # S = log(rho(E_typical))
    # E_typical = <E> at temperature beta
    E_mean = np.sum(ev * np.exp(-beta * ev)) / np.sum(np.exp(-beta * ev))

    # Density of states at E_mean (from level spacing)
    # rho(E) ~ 1/<level spacing at E>
    sorted_ev = np.sort(ev)
    idx = np.searchsorted(sorted_ev, E_mean)
    if idx > 0 and idx < len(sorted_ev):
        dE = sorted_ev[idx] - sorted_ev[idx-1]
        rho = 1 / dE
        S = np.log(rho)
    else:
        S = np.nan
    return S, E_mean


# =============================================================================
# Compute entropy vs beta for SYK q=4 N=12
# =============================================================================
print("\n" + "="*72)
print("PART 1: ENTROPY vs BETA (SYK q=4 N=12)")
print("="*72)

gammas = build_majoranas(12)
H = build_H_SYK_q4(gammas, seed=42)
ev = eigh(H, eigvals_only=True)
ev = ev - ev.min() + 0.1

betas = np.logspace(-1, 2, 30)
print(f"\n{'beta':>10} {'<E>':>14} {'rho(<E>)':>14} {'S = log rho':>14}")
print("-"*60)
results_18 = []
for beta in betas:
    S, E_mean = entropy_replica(ev, beta)
    results_18.append((beta, E_mean, S))
    print(f"{beta:>10.3f} {E_mean:>14.4e} {'-':>14} {S if not np.isnan(S) else 0:>14.4f}")

# =============================================================================
# Liouville entropy (analytical, for c=1)
# =============================================================================
print("\n" + "="*72)
print("PART 2: LIOUVILLE ENTROPY (c=1, ANALYTICAL)")
print("="*72)

# For c=1 Liouville, the entropy is the Cardy formula:
# S = 2 pi sqrt(c L / 6) for L >> c
# where L is the energy in units where c=1

# S_Cardy = 2 pi sqrt(L / 6) for c=1
print("\nCardy formula for c=1 CFT: S = 2 pi sqrt(L / 6)")
print(f"\n{'L (energy)':>14} {'S_Cardy':>14}")
print("-"*40)
for L in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    S = 2 * PI * np.sqrt(L / 6)
    print(f"{L:>14.3e} {S:>14.4f}")

# =============================================================================
# f_back from entropy?
# =============================================================================
print("\n" + "="*72)
print("PART 3: f_back FROM ENTROPY?")
print("="*72)

# f_back is the "back-projection" factor from 2D to 3+1D
# In SIDC: f_back = 10^-85
# The interpretation: of all events on the 2D brane, only ~10^-85 fraction
# projects back to 3+1D as observable

# From the entropy: if S is the number of accessible states, then
# f_back ~ 1 / S^something?

# Try: f_back = exp(-S) where S is the 2D entropy
# For SN (E ~ 10^44 J = 10^35 in Planck units):
# S_Cardy = 2 pi sqrt(10^35 / 6) ~ 2 pi * 4e17 ~ 2.5e18
# exp(-S) ~ exp(-2.5e18) ~ 0 (way too small)

# Try: f_back = exp(-S_2D / N) where N=12
# For SN: S_2D/N ~ 2.1e17, exp(-2.1e17) ~ 0 (still too small)

# Try: f_back = exp(-S_2D / S_typical)
# where S_typical ~ log(dim Hilbert space) = log(2^6) = 4.16 for N=12
# S_2D/S_typical ~ 2.5e18 / 4 ~ 6e17, exp(-6e17) ~ 0

# Conclusion: f_back is NOT a simple exponential of entropy

print("Attempted: f_back = exp(-S_2D)")
print("For SN: S_2D ~ 10^18, exp(-10^18) ~ 0")
print("WAY too small. f_back is NOT exp(-S).")

print("\nAttempted: f_back = (E_4D/E_2D)^{...}")
print("This matches the SIDC formula: f_back ~ (E_4D/E)^{1/(2 alpha)}")
print("From v10: f_back = 8.76e-86 ~ 10^-85")

# =============================================================================
# Replica trick on Liouville
# =============================================================================
print("\n" + "="*72)
print("PART 4: REPLICA TRICK ON LIOUVILLE (c=1)")
print("="*72)

# For c=1 Liouville on the torus, the n-replica partition function is:
# Z_n(q) = sum_p chi_p(q^n) where chi_p is a character and q = exp(-2 pi tau_2)
#
# For n=1: Z_1 = sum_p chi_p(q)
# For n=2: Z_2 = sum_p chi_p(q^2)
# Entropy S = -d/dn log Z_n |_{n=1}

# Simplified: just compute Z_n for the vacuum character
# chi_0(q) = (1-q)(1-q^2).../(q^(1/24)) for c=1

# Use modular parameter q
print("\nFor c=1 Liouville vacuum character:")
print("  chi_0(q) = eta(tau) / q^(1/24) where eta is Dedekind eta")
print(f"\n{'n':>4} {'Z_n (approx)':>14} {'-d/dn log Z_n':>14}")
print("-"*50)

q = 0.5  # arbitrary modular parameter
def chi_0(q_val, n_terms=20):
    """Vacuum character for c=1."""
    eta = np.prod([(1 - q_val**k) for k in range(1, n_terms+1)])
    return eta / q_val**(1/24)

for n in [1, 2, 3, 5, 10]:
    Z_n = chi_0(q**n)
    print(f"{n:>4} {Z_n:>14.4e} {'-':>14}")

# =============================================================================
# Verdict
# =============================================================================
print("\n" + "="*72)
print("PART 5: VERDICT (v18)")
print("="*72)
print("""
REPLICA TRICK FOR f_back (v18):
  + Computed entropy vs beta for SYK q=4 N=12 (from density of states)
  + Computed Liouville entropy (Cardy formula for c=1)
  + Attempted to derive f_back from entropy

WHAT v18 SHOWS:
  - SYK entropy S(E) is well-defined (from level spacing)
  - Liouville entropy is S_Cardy ~ sqrt(L) for c=1
  - f_back is NOT simply exp(-S); the entropies are too large

WHAT v18 DOES NOT SHOW:
  - Direct derivation of f_back from S(E)
  - Connection between entropy and back-projection factor
  - Replica trick doesn't close L48

CONCLUSION:
  - f_back remains a calibrated parameter
  - Its value 10^-85 matches SIDC's composite formula (§3.60)
  - But it's NOT derived from entropy in this v18
  - L48 (closed for form, calibrated for value) status unchanged
""")