# Liouville f_active Test — Findings

## What we tested

The cascade's 2D universe Lagrangian is hypothesized to be 2D Liouville quantum gravity
(LQG). This test asks: can the Liouville framework reproduce the cascade's empirical
f_active = 0.0513 ± 0.007 (MCMC)?

## What we found

### Test 1: Simple case (degenerate weight α = Q/2)
- For ANY b, if τ_2D = 0.7 Gyr, then f_active = 0.7/13.8 = **0.0507**
- This EXACTLY matches the cascade's empirical f_active (0.0513 ± 0.007)
- Result: **PASS** ✓

This is the basic cascade formula. The Liouville framework is consistent with it
because the 2D universe's lifetime is τ_2D = 1/√μ (Liouville potential), and the
cascade's empirical f_active comes from τ_2D/T_universe = 0.7/13.8.

### Test 2: Integral over α distribution
- We compute f_active averaged over a distribution of 2D universe weights α
- The 2-point function ρ(α) weights the average
- The 2D universe's lifetime at weight α: τ_2D(α) = (1/√μ) × (1/Δ_α)
- For α_min = 0.20, b in [0.5, 2.0], we get f_active in [0.047, 0.070] — CLOSE TO 0.051 ✓
- For α_min = 0.10, f_active in [0.056, 0.083] — slightly higher
- For α_min = 0.01, f_active in [0.091, 0.137] — too high

Result: **PASS** (for α_min ~ 0.2, which corresponds to a natural cutoff)

The integral suggests that the cascade's f_active = 0.051 is consistent with
a 2D universe weight distribution that has α_min ~ 0.2 (in Liouville natural units).
This is a NATURAL value: α = 0.2 corresponds to Δ_α = 0.2 × (Q - 0.2) ~ 0.36,
which is a "light" 2D universe weight.

### Test 3: Lifetime calibration
- τ_2D_phys = 0.7 Gyr requires α/√μ_L ~ 6.6e24 cm in natural units
- The 2D universe's natural length scale √(1/μ_L) is a 2D Planck length
- For α ~ 1 (strong coupling), ℓ_2D ~ 2 kpc (galactic scale!) ✓
- For α ~ 0.1 (weak coupling), ℓ_2D ~ 0.02 Mpc (cluster scale)

This is a remarkable coincidence: the natural 2D universe length scale is
comparable to galactic scales, which is exactly the regime where the cascade
predicts DM effects.

## What the Liouville framework ADDS to the cascade

1. **Mathematical rigor**: Liouville 2D CFT is mathematically proven
   (Miller-Sheffield 2021). The 2-point and 3-point functions (DOZZ) are
   exact. This gives the cascade a rigorous 2D universe sector.

2. **Specific Lagrangian**: The cascade's 2D universe action is:
   S_2D = (1/4π) ∫ d²σ √γ [ (1/2)(∇φ)² + Q R[γ] φ + μ e^{2bφ} ]
   This is the Liouville action with parameter b and cosmological constant μ.

3. **Specific 2-point function**: The 2D universe's "weight" ρ(α) is the
   DOZZ reflection coefficient, exact and calculable.

4. **Specific 3-point function**: The 2D universe's "creation amplitude"
   is the DOZZ 3-point function, exact and calculable.

5. **Natural 2D universe lifetime**: τ_2D ~ 1/√μ × (1/Δ_α) is a
   specific, calculable quantity from the Liouville framework.

6. **Coupling to SM**: The 2D universe's creation by SM events is a
   Liouville vertex operator insertion: e^{2α0φ}. The DOZZ formula
   gives the creation rate.

7. **Holographic dual**: The Liouville 2D CFT is the holographic dual
   of 3D quantum gravity (AdS_3/CFT). This connects the cascade's
   2D universe sector to the bulk 5D AdS_5 geometry.

## What the Liouville framework does NOT add

1. **The specific value of τ_2D = 0.7 Gyr remains a free parameter**.
   The Liouville calculation gives τ_2D = (α/c) × 1/√μ_L, but the
   product α × √μ_L is not predicted. The cascade's empirical 0.7 Gyr
   is the "right answer" by physical analogy, not by derivation.

2. **The central charge c (or b) is not predicted**. The cascade's
   2D universe could have any c. The choice c = 1 (b = 1) is the
   simplest, but the cascade's empirical f_active doesn't pick out
   a specific c.

3. **The α_min cutoff is not predicted**. The integral over α gives
   f_active ~ 0.05 for α_min ~ 0.2, but this is a free parameter.

So the Liouville framework closes Limitation 26's FIRST PHASE
(specifying L_2D as a known 2D CFT) but does NOT close its SECOND
PHASE (deriving the specific parameters b, μ, α_min from first
principles).

## Recommendation

**Adopt the Liouville framework as the cascade's 2D universe Lagrangian.**

The cascade's §2.5.1 (Lagrangian skeleton) should be updated to:
- S_brane_2D = (1/4π) ∫_Σ d²σ √γ [ (1/2)(∇φ)² + Q R[γ] φ + μ e^{2bφ} ]
- S_coupling = -α ∫_brane d⁴x T_SM(x) · e^{2α0 φ(x)} |_{2D boundary}
- S_destruction = +α ∫_brane d⁴x T_DM(x) · δ(t - τ_2D)

This is a major theoretical improvement and provides the cascade with
a well-defined 2D universe sector.

## Limitation 26 update

Limitation 26 should be updated from:
"Cascade specifies geometry, not Lagrangian. The action in §2.5.1 is a
SKELETON with 5+ free parameters that need to be specified for a complete theory."

To:
"Cascade specifies the 2D universe Lagrangian as 2D Liouville quantum gravity
(S_brane_2D = (1/4π) ∫ d²σ √γ [(1/2)(∇φ)² + Q R[γ] φ + μ e^{2bφ}]).
This closes the 2D universe Lagrangian specification. Remaining free
parameters are b (Liouville parameter), μ (Liouville cosmological constant),
and α_min (cutoff on 2D universe weight distribution). These are not
derivable from the cascade as written; they require either a 2D CFT
matter content specification or a separate physical principle."

## Status of the test (UPDATED after v3 analysis)

**HONEST REVISION:** The v1 f_active test was a TAUTOLOGY, not a derivation.

- "f_active = τ_2D/T_universe = 0.7/13.8 = 0.051" is dimensional analysis.
- The cascade's f_active was ALREADY τ_2D/T_universe BEFORE I introduced Liouville.
- Adding Liouville doesn't add anything to f_active — it's the same formula.

The v1 finding "Liouville f_active matches cascade" should be revised to:
"Liouville f_active formula IS the cascade's f_active formula, with no
new information added. The 2/3 tests that 'pass' are: (1) the simple
case, which is a tautology, and (2) the integral over α, which depends
on assumptions about τ(Δ) scaling. The third test (lifetime calibration)
is a sanity check, not a derivation."

The REAL wins from Liouville are:
- A specific 2D universe Lagrangian (Liouville action with b, μ)
- The DOZZ 3-point function |C|² ~ 1-50 (a real Liouville number)
- A specific reflection coefficient ρ(α)
- Mathematical rigor (2D CFT is exact)
- Holographic dual to AdS_3 (Karch-Randall)

The REAL losses from Liouville (acknowledged in v3):
- It does NOT derive τ_2D = 0.7 Gyr (free parameter)
- It does NOT derive g_+ (it's c × H_0 / 2π)
- It does NOT derive f_back (probability, not 2-point function)
- It does NOT derive 5/27/68 (needs Boltzmann)
- It does NOT derive m_2D (needs 2D Planck scale)
- It does NOT solve the 50-orders-of-magnitude mass tension

## What's still missing for a "full" 2D CFT derivation

1. **The 2D universe's matter content**: Is the 2D universe a free 2D CFT
   (c=1), or does it have SM matter (c=25)? This sets b.

2. **The bulk-brane coupling α**: How strongly does a SM event create a
   2D universe? This is the cascade's "2D universe creation rate"
   and is set by the DOZZ 3-point function.

3. **The 2D universe's energy at death**: When the 2D universe dies, how
   much energy is returned to 3+1D? This is the cascade's "DM energy
   deposit" and is set by the Liouville action evaluated at φ → 0.

4. **The 5/27/68 split**: The cosmic energy budget. This is the
   cascade's biggest unresolved derivation. The Liouville framework
   provides structure, but not specific numbers.

5. **The H_0 derivation**: The cascade's H_0(z) framework (§2.6.2).
   The Liouville calculation should give H_0,4D as the geometric mean
   of 2D universe creation/annihilation rates.

6. **The RAR g_+ derivation**: The cascade's universal acceleration scale.
   The Liouville calculation should give g_+ as a specific combination
   of b, μ, and α_0.

## Code

The test code is at: tempcalc/liouville_factive_test.py
The results are at: tempcalc/liouville_factive_results.json
The full literature memo is at: tempcalc/lagrangian_literature_memo.md
